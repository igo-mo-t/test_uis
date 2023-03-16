"""data filling

Revision ID: 6651859774b5
Revises: 
Create Date: 2023-03-15 17:30:06.557015

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData

# revision identifiers, used by Alembic.
revision = '6651859774b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    meta.reflect(only=('accrual', 'payment'))
    accrual = Table('accrual', meta)
    payment = Table('payment', meta)
    
    
    op.bulk_insert(
        accrual,
        [
            {'id':1, 'date':'2023-01-25', 'month':1},
            {'id':2, 'date':'2023-02-25', 'month':2},
            {'id':3, 'date':'2023-03-25', 'month':3},
            {'id':4, 'date':'2023-04-25', 'month':4},
            {'id':5, 'date':'2023-04-27', 'month':4},
            {'id':6, 'date':'2023-05-25', 'month':5},
            {'id':7, 'date':'2023-05-27', 'month':5}
        ])

    op.bulk_insert(
        payment,
        [
            {'id':1, 'date':'2023-03-28', 'month':3},
            {'id':2, 'date':'2023-04-28', 'month':4},
            {'id':3, 'date':'2023-04-29', 'month':4},
            {'id':4, 'date':'2023-05-27', 'month':5},
            {'id':5, 'date':'2023-06-28', 'month':6},
            {'id':6, 'date':'2023-06-29', 'month':6},
            {'id':7, 'date':'2023-07-25', 'month':7},
            {'id':8, 'date':'2023-07-28', 'month':7},
            {'id':9, 'date':'2023-08-25', 'month':8},
            {'id':10, 'date':'2023-09-25', 'month':9}
        ])



