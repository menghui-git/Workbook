from rest_framework import serializers

from notes.models import UserWord
from vocab.models import Word


class UserWordSerializer(serializers.ModelSerializer):
    _word = serializers.CharField(source='word.name', read_only=True)

    class Meta:
        model = UserWord
        fields = ('id', '_word')

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        try:
            ret['word_name'] = data['word']
            # ret['user_id'] = data['user_id']
        except KeyError:
            raise
        return ret

    def create(self, validated_data):
        word_name = validated_data.pop('word_name')
        word, _ = Word.objects.get_or_create(name=word_name)
        # validated_data['word'] = word
        instance, _ = UserWord.objects.get_or_create(word=word)
        return instance
