# ============================================================
# CONFIGURACION DE PARAMETROS
# ============================================================
#
# Define el tamaño del valor DESENCRIPTADO / valor de negocio
# para cada parámetro cuando Swagger no proporciona
# minLength y maxLength.
#
# Cuando el $ref del schema contiene "encrypted", el tamaño
# se muestra como "Variable" sin importar estos valores.
#
# Excepción: X-Ct siempre es "Variable" sin importar
# el estado de encriptación del request.
# ============================================================

PARAMETER_CONFIG = {
    "X-Ct": {
        "type": "string",
        "size": "Variable",
    },
    "email": {
        "type": "string",
        "size": "20",
    },
    "userName": {
        "type": "UUID V4",
        "size": "Según Estándar",
    },
    "statusCode": {
        "type": "number",
        "size": "3 ",
    },
    "code": {
        "type": "string",
        "size": "5 ",
    },
    "data": {
        "type": "object",
        "size": "---",
    },
    "message": {
        "type": "string",
        "size": "50 ",
    },
    "users": {
        "type": "array",
        "size": "100",
    },
    "user": {
        "type": "object",
        "size": "---",
     },
    "userAttributes": {
        "type": "object",
        "size": "---",
     },
    "profilePictureUrl": {
        "type": "string",
        "size": "Variable ",
    },
    "presignedPostProfileImage": {
        "type": "object",
        "size": "---",
        },
    "password": {
        "type": "string",
        "size": "8 ",
    },
    "newPassword": {
        "type": "string",
        "size": "8 ",
    },
    "confirmationCode": {
        "type": "string",
        "size": "6 ",
    },
    "otp": {
        "type": "string",
        "size": "6 ",
    },
    "phone": {
        "type": "string",
        "size": "15 ",
    },
    "name": {
        "type": "string",
        "size": "20 ",
    },
    "documentNumber": {
        "type": "string",
        "size": "12",
    },
    "role": {
        "type": "string",
        "size": "20 ",
    },
    "userRole": {
        "type": "string",
        "size": "50 ",
    },
    "bio_code": {
        "type": "string",
        "size": "20 ",
    },
    "bio_status": {
        "type": "string",
        "size": "15 ",
    },
    "kyc_level": {
        "type": "string",
        "size": "10",
    },
    "isAcceptATDP": {
        "type": "boolean",
        "size": "----",
    },
    "lastKey": {
        "type": "string",
        "size": "25 ",
    },
    "phone_number": {
    "type": "string",
    "size": "15",
    },
    "custom_documentNumber": {
        "type": "string",
        "size": "15 ",
    },
    "custom_documentType": {
        "type": "string",
        "size": "15",
    },
    "custom_firstName": {
        "type": "string",
        "size": "25",
    },
    "custom_lastName": {
        "type": "string",
        "size": "25 ",
    },
    "custom_nickname": {
        "type": "string",
        "size": "25",
    },
    "custom_country": {
        "type": "string",
        "size": "25",
    },
    "custom_documentCountry": {
        "type": "string",
        "size": "20",
    },
    "amount": {
        "type": "number",
        "size": "Variable"
    },
    "buyer": {
        "type": "string",
        "size": "25",
    },
    "seller": {
        "type": "string",
        "size": "25",
    },
    "atdpType": {
        "type": "string",
        "size": "10",
    },
    "idTemplate": {
        "type": "string",
        "size": "Variable"
    },
    "pin": {
        "type": "string",
        "size": "6",
    },
    "hash": {
        "type": "string",
        "size": "Variable",
        },
    "enabled": {
        "type": "boolean",
        "size": "----",
    },
    "url": {
        "type": "string",
        "size": "Variable",
    },
    # ============================================================
    # MICROSERVICIO EVENTS
    # ============================================================
    "userId": {
        "type": "UUID V4",
        "size": "Según Estándar",
    },
    "username": {
        "type": "string",
        "size": "25",
    },
    "payload": {
        "type": "object",
        "size": "---",
    },
    "title": {
        "type": "string",
        "size": "50 ",
    },
    "link": {
        "type": "string",
        "size": "Variable",
    },
    "type": {
        "type": "string",
        "size": "20",
    },
    "notificationId": {
        "type": "string",
        "size": "50",
    },
    "notification": {
        "type": "object",
        "size": "---",
    },
    "id": {
        "type": "UUID V4",
        "size": "Según Estándar",
    },
    "read": {
        "type": "boolean",
        "size": "----",
    },
    "timestamp": {
        "type": "string",
        "size": "Variable",
    },
    "success": {
        "type": "boolean",
        "size": "----",
    },
    "redirectTo": {
        "type": "string",
        "size": "Variable",
    },
    # ============================================================
    # MICROSERVICIO WALLET
    # ============================================================
    "balances": {
        "type": "array",
        "size": "100",
    },
    "detailTokens": {
        "type": "array",
        "size": "100",
    },
    "symbol": {
        "type": "string",
        "size": "100",
    },
    "stablecoin": {
        "type": "string",
        "size": "10",
    },
    "country": {
        "type": "string",
        "size": "3",
    },
    "status": {
        "type": "string",
        "size": "10",
    },
    "balancePol": {
        "type": "object",
        "size": "---",
    },
    "features": {
        "type": "object",
        "size": "---",
    },
    "balance": {
        "type": "number",
        "size": "Variable",
    },
    "tokensBalance": {
        "type": "number",
        "size": "Variable",
    },
    "totalTokens": {
        "type": "number",
        "size": "Variable",
    },
    "tokenPriceInUSD": {
        "type": "number",
        "size": "Variable",
    },
    "walletAddress": {
        "type": "string",
        "size": "Variable",
    },
    "address": {
        "type": "string",
        "size": "Variable",
    },
    # ============================================================
    # MICROSERVICIO VAULTS
    # ============================================================
    "salesStatus": {
        "type": "string",
        "size": "9",
    },
    "search": {
        "type": "string",
        "size": "50",
    },
    "vaultType": {
        "type": "string",
        "size": "50",
    },
    "trend": {
        "type": "string",
        "size": "50",
    },
    "limit": {
        "type": "number",
        "size": "50",
    },
    "owner": {
        "type": "string",
        "size": "36",
    },
    "buyLimit": {
        "type": "object",
        "size": "---",
    },
    "buyMinLimit": {
        "type": "object",
        "size": "---",
    },
    "essential": {
        "type": "number",
        "size": "50",
    },
    "advanced": {
        "type": "number",
        "size": "50",
    },
    "premium": {
        "type": "number",
        "size": "50",
    },
    "initialSupply": {
        "type": "number",
        "size": "50",
    },
    "availableStock": {
        "type": "number",
        "size": "50",
    },
    "valueInUSD": {
        "type": "number",
        "size": "50",
    },
    "description": {
        "type": "string",
        "size": "500",
    },
    "additionalInfo": {
        "type": "object",
        "size": "---",
    },
    "coordinates": {
        "type": "object",
        "size": "---",
    },
    "lng": {
        "type": "string",
        "size": "50",
    },
    "lat": {
        "type": "string",
        "size": "50",
    },
    "assetIndicators": {
        "type": "array",
        "size": "100",
    },
    "displayName": {
        "type": "string",
        "size": "50",
    },
    "values": {
        "type": "array",
        "size": "100",
    },
    "value": {
        "type": "number",
        "size": "50",
    },
    "icon": {
        "type": "string",
        "size": "50",
    },
    "units": {
        "type": "string",
        "size": "50",
    },
    "includeImages": {
        "type": "boolean",
        "size": "----",
    },
    "includeDocs": {
        "type": "boolean",
        "size": "----",
    },
    "mainImage": {
        "type": "string",
        "size": "100",
    },
    "publicDocs": {
        "type": "array",
        "size": "100",
    },
    "videoLink": {
        "type": "string",
        "size": "50",
    },
    "strategicLocation": {
        "type": "string",
        "size": "100",
    },
    "adminUserName": {
        "type": "string",
        "size": "36",
    },
}
