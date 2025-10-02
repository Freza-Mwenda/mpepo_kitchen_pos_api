import random
import time
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.database import get_db
from dtos.order_dtos import Order, OrderCreate
from services.invoices.invoice_service import create_invoice_log, update_invoice_log
from services.orders.orders_service import create_order, get_orders

router = APIRouter()

# Enhanced order creation with auto-tax submission
@router.post("", response_model= Order)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        order_data = order.dict()
        # Convert Pydantic models to dict for proper JSON serialization
        if 'items' in order_data and isinstance(order_data['items'], list):
            order_data['items'] = [
                {
                    'product': item['product'],
                    'quantity': item['quantity']
                }
                for item in order_data['items']
            ]

        # Create order in database
        db_order = create_order(db, order_data)

        # AUTO-TAX SUBMISSION (Student B requirement)
        try:
            print(f"🔄 Auto-submitting order {db_order.id} to tax authority...")

            # Prepare invoice data for tax authority
            tax_invoice_data = {
                "invoice_number": f"MPEPO-{db_order.id}",
                "issue_date": db_order.created_at.isoformat(),
                "seller_info": {
                    "name": "Mpepo Kitchen",
                    "tin": "P051234567L",
                    "address": "Nairobi, Kenya"
                },
                "buyer_info": {
                    "name": "Retail Customer",
                    "tin": "000000000",
                    "address": "Walk-in Customer"
                },
                "items": [
                    {
                        "description": f"{item['product']['name']}",
                        "quantity": item['quantity'],
                        "unit_price": float(item['product']['price']),
                        "total_amount": float(item['product']['price']) * item['quantity'],
                        "tax_amount": float(item['product']['price']) * item['quantity'] * 0.16,
                        "tax_code": "A"
                    }
                    for item in order_data['items']
                ],
                "summary": {
                    "subtotal": float(db_order.subtotal),
                    "tax_amount": float(db_order.tax_amount),
                    "total": float(db_order.total),
                    "currency": "KES"
                },
                "tax_breakdown": {
                    "vat_rate": 0.16,
                    "vat_amount": float(db_order.tax_amount)
                }
            }

            # Submit to tax authority - SYNC VERSION
            tax_response = submit_to_tax_authority(tax_invoice_data)

            # Update order with tax reference if successful
            if tax_response.get("success"):
                db_order.tax_authority_ref = tax_response.get("authority_reference")
                db.commit()
                print(f"✅ Tax submission successful for order {db_order.id}")
                print(f"   Tax Reference: {db_order.tax_authority_ref}")

                # Log the invoice submission
                create_invoice_log(db, db_order.id, tax_invoice_data)
                update_invoice_log(db, db_order.id, tax_response, "submitted")

            else:
                print(f"❌ Tax submission failed for order {db_order.id}: {tax_response.get('error_message')}")
                # Log the failed attempt
                create_invoice_log(db, db_order.id, tax_invoice_data)
                update_invoice_log(db, db_order.id, tax_response, "failed")

        except Exception as tax_error:
            print(f"⚠️ Tax submission error for order {db_order.id}: {tax_error}")
            import traceback
            print(f"Full error: {traceback.format_exc()}")
            # Continue with order creation even if tax submission fails

        return db_order

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating order: {str(e)}")


@router.get("", response_model=List[Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_orders(db, skip=skip, limit=limit)

# Synchronous tax authority endpoint
@router.post("/tax-authority/submit")
def submit_to_tax_authority(invoice_data: dict):
    """
    Synchronous mock tax authority endpoint with proper invoice validation
    """
    import uuid

    # Simulate processing time
    time.sleep(1.5)

    # Validate required fields
    required_fields = ['invoice_number', 'seller_info', 'buyer_info', 'items', 'summary']
    for field in required_fields:
        if field not in invoice_data:
            return {
                "success": False,
                "error_message": f"Missing required field: {field}",
                "timestamp": time.time()
            }

    # Validate seller info
    seller_info = invoice_data.get('seller_info', {})
    if 'tin' not in seller_info or not seller_info['tin']:
        return {
            "success": False,
            "error_message": "Seller TIN is required",
            "timestamp": time.time()
        }

    # Simulate random failures (more realistic)
    success_rate = 0.85  # 85% success rate
    success = random.random() < success_rate

    if success:
        # Generate realistic tax authority response
        invoice_number = f"TAX-INV-{int(time.time())}-{random.randint(1000, 9999)}"
        authority_ref = f"KRA-REF-{uuid.uuid4().hex[:12].upper()}"

        # Log the successful submission
        print(f"✅ Tax invoice submitted successfully: {invoice_number}")
        print(f"   Authority Reference: {authority_ref}")
        print(f"   Total Amount: {invoice_data.get('summary', {}).get('total', 0)}")
        print(f"   Tax Amount: {invoice_data.get('summary', {}).get('tax_amount', 0)}")

        return {
            "success": True,
            "invoice_number": invoice_number,
            "authority_reference": authority_ref,
            "timestamp": time.time(),
            "message": "Invoice successfully submitted to Kenya Revenue Authority",
            "submission_id": f"SUB-{int(time.time())}",
            "qr_code_url": f"https://api.kra.go.ke/qr/{authority_ref}"
        }
    else:
        # Simulate different error scenarios
        errors = [
            "Tax authority service temporarily unavailable",
            "Invalid seller TIN provided",
            "Invoice total below minimum threshold",
            "Network timeout with tax authority server",
            "Tax authority system undergoing maintenance",
            "Duplicate invoice number detected"
        ]
        error_message = random.choice(errors)

        print(f"❌ Tax submission failed: {error_message}")

        return {
            "success": False,
            "error_message": error_message,
            "retry_after": 300,
            "timestamp": time.time(),
            "error_code": f"ERR-{random.randint(1000, 9999)}"
        }