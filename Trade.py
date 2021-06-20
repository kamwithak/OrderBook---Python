class Trade(object):
    def __init__(self, incoming_side, incoming_price, trade_size, incoming_order_id, book_order_id):
        self.side = incoming_side
        self.price = incoming_price
        self.size = trade_size
        self.incoming_order_id = incoming_order_id
        self.book_order_id = book_order_id

    def __repr__(self):
        return 'Executed: {0} {1} units at {2}'.format(self.side, self.size, self.price)
