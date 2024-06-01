from starlette.responses import Response
from starlette import status

from orders.app import app

order={
    'id': 1,
    'status': "created"
}

@app.post('/app', status_code=status.HTTP_201_CREATED)
def create_order():
    return order
