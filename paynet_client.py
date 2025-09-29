import os
import uuid

def create_invoice(amount, user_id):
    invoice_id = str(uuid.uuid4())
    # Bu joyda haqiqiy Paynet API integratsiyasi bo‘lishi kerak
    return {
        "id": invoice_id,
        "link": f"https://paynet.test/invoice/{invoice_id}?amount={amount}"
  }
