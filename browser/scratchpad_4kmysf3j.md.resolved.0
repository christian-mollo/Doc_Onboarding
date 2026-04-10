# API Audit Findings - Final Iteration

## 1. OAuth2 Authentication (GetToken)
- **Endpoint**: `{{BASIC__URL}}/auth/realms/digital_identity/protocol/openid-connect/token`
- **Method**: POST
- **Payload**: `client_id=digital-identity`, `username`, `password`, `grant_type=password`, `client_secret` (URL-encoded)
- **Response**: Contains `access_token`, `refresh_token`, `expires_in`, `refresh_expires_in`.
- **Note**: The presence of `refresh_token` confirms support for session renewal without re-authentication.

## 2. OCR Endpoint (Get OCR)
- **URL**: `{{BASIC_URL}}/api/ms-digital-identity-profirma/getOCR`
- **Error Pattern (400)**: Returning a root level `message`, `data: null`, and a detailed `error` string containing technical stack traces (Jackson exceptions).
- **Error Pattern (401)**: Returns `{"error": "unauthorized", "error_description": "Full authentication is required to access this resource"}`.

## 3. Double Identity Endpoint (Create Double Identity)
- **URL**: `{{BASIC_URL}}/api/ms-digital-identity-profirma/createDoubleIdentity`
- **Error Pattern (400)**: Root property `code: 400`, `message: "BAD_REQUEST"`, and `data.status.status` containing `message: "FORMATO DE BODY NO VÁLIDO"`.
- **Validation**: Strict uppercase requirements for all fields except email and image formats.

## 4. General Observations
- **Missing Endpoints**: No endpoints related to 'Firma Digital', 'PDF', or 'Sign' were found in this specific collection.
- **Headers**: No custom headers like `X-App-Version` or `X-Tenant-Id` were detected in snippets or documentation.
- **Data Integrity**: Global rule that all data must be in UPPERCASE.

## 5. Development Rules & Competencies
1. **Validation Domain**: Implement a pre-processor to enforce UPPERCASE on all string fields (except excluded ones) before calling the external API.
2. **Error Handling**: Implement custom Jackson deserializers to handle inconsistent error structures between OCR and Identity endpoints.
3. **Resilience**: Use `CircuitBreaker` and `Retry` for OCR calls given the "heavy" nature of base64 processing.
4. **Security**: Store `client_secret` and `password` in a secure vault (e.g., AWS Secrets Manager, HashiCorp Vault), never in code or plain `.env`.
5. **Auditability**: Every call must include a `correlation-id` passed from the frontend and logged in every step of the backend service.
