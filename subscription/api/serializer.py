from rest_framework import serializers

from subscription.models import Membership, Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only = ['is_active']

    

class MembershipSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=True)
    class Meta:
        model = Membership
        fields = '__all__'
        read_only = ['created_at', 'updated_at']

    # for displaying trainer, member, subscription name in response    
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
        data['trainer'] = instance.trainer.full_name if instance.trainer else None
        return data
    

    def create(self, validated_data):
        print(validated_data)
        one_day_price = validated_data['subscription'].price / validated_data['subscription'].days
        validated_data['price']=validated_data['days']*one_day_price
        return super().create(validated_data)
    





