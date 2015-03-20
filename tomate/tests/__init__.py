from __future__ import unicode_literals


class SubscriptionMixin(object):

    def test_subscriptions(self):
        obj = self.create_instance()

        for (_, method) in obj.subscriptions:
            getattr(obj, method)(None, a=1, b=2, c=3)

    def create_instance(self):
        raise NotImplementedError()
