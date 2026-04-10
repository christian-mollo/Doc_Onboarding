# Inventario de Datos e Información: Identidad y Firma v3

Este documento detalla exhaustivamente todos los datos gestionados por la API, clasificados por su naturaleza y nivel de sensibilidad, bajo estándares de protección de datos bancarios.

## 1. Datos de Autenticación y Acceso
Información necesaria para establecer una sesión segura con los servicios.
- **Credenciales**: `username`, `password`.
- **Identificadores de Aplicación**: `client_id` (digital-identity), `client_secret`.
- **Tokens de Sesión**: `access_token` (JWT), `refresh_token`, `token_type` (Bearer).
- **Parámetros OAuth2**: `grant_type`, `realm`.

## 2. Información de Identidad (PII Extraída)
Datos personales sensibles capturados mediante el proceso de OCR de la Cédula de Identidad.
- **Imágenes del Documento**: `obverseData` (Anverso CI), `reverseData` (Reverso CI) en formato **Base64**.
- **Atributos de Identidad**:
  - `givenNames`: Nombres del titular (MAYÚSCULAS).
  - `surname1`: Primer Apellido (MAYÚSCULAS).
  - `surname2`: Segundo Apellido (MAYÚSCULAS).
  - `idNumber`: Número de Cédula de Identidad (Numérico).
  - `complement`: Letra de complemento (si aplica).
  - `birthDate`: Fecha de nacimiento (Formato ISO).
  - `issuePlace`: Lugar de expedición (Códigos de 2 letras, ej: LP, SC).
  - `nationality`: Nacionalidad (MAYÚSCULAS).
  - `gender`: Género (Masculino/Femenino).

## 3. Datos Biométricos (Alta Sensibilidad)
Información utilizada para la validación de prueba de vida y biometría facial.
- **Imagen de Rostro**: `personalBiography` (Selfie en **Base64**, < 1MB).
- **Formatos**: `selfieFormat` (ej: `JPG`, `PNG`).
- **Resultado de Validación**: `verificationResult` (Código de éxito/falla biométrica).

## 4. Datos Operativos y Metadatos
Información técnica para la trazabilidad y auditoría de la transacción.
- **Identificadores de Flujo**:
  - `transactionId`: ID único de transacción bancaria (Snowflake ID).
  - `token`: Identificador temporal para el proceso de OCR (30 min).
  - `verification_token`: Token de cierre de proceso, obligatorio para firma digital (24 horas).
- **Estado de Proceso**: `status` (SUCCESS, FAILED), `message`, `code` (406, 408, 412).
- **Trazabilidad de Red**: `X-Correlation-Id`, `IP de origen`, `Timestamp`.

## 5. Variables de Entorno y Configuración
Datos técnicos de infraestructura.
- **Base URLs**: `{{BASE_URL_IDENTIDAD}}`, `{{BASIC_URL}}`.
- **Entornos**: `DESARROLLO`, `PRODUCCIÓN`.

---
> [!IMPORTANT]
> Los datos en la categoría **2 (PII)** y **3 (Biometría)** deben ser enmascarados en logs y cifrados en tránsito (TLS 1.2+) siguiendo la política de seguridad Zero Trust definida para el backend.
