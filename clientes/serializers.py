from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_validation, nome_validation, rg_validation, celular_validation


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_validation(data["cpf"]):
            raise serializers.ValidationError({"Cpf": "PF inválido"})
        if not nome_validation(data["nome"]):
            raise serializers.ValidationError({"nome": "Caractere inválido"})
        if not rg_validation(data["rg"]):
            raise serializers.ValidationError({"rg":"O RG deve conter 9 dígitos"})
        if not celular_validation(data["celular"]):
            raise serializers.ValidationError({"celular":"O celular deve conter 11 dígitos: xx xxxxx-xxxx"})
        return data
