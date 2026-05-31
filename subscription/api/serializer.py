from rest_framework import serializers

from subscription.models import Membership, Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only = ['is_active']

    

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
        read_only = ['created_at', 'updated_at']
        
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        full_name = " ".join(
        filter(
            None,
            [
                instance.member.first_name,
                instance.member.middle_name,
                instance.member.last_name
            ]
        )
    )

        data['member'] = full_name
        data['subscription'] = instance.subscription.name
        data['trainer'] = full_name
        return data



