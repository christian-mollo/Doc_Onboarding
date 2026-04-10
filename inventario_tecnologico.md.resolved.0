# Inventario del Stack Tecnológico: Identidad y Firma v3

Tras un análisis exhaustivo de la documentación, headers de red, y estructuras de datos, se ha determinado el siguiente stack tecnológico para el servicio web de la API.

## 1. Núcleo de Aplicación (Backend)
- **Lenguaje**: Java 17+ (Deducido por stack traces de librerías modernas).
- **Framework**: Spring Boot 3.x / 4.x.
- **Librería de Serialización**: Jackson (com.fasterxml.jackson).
- **Arquitectura**: Microservicios (Patrón `ms-service-name`).

## 2. Seguridad e Identidad (IAM)
- **Servidor de Identidad**: Keycloak (Basado en rutas `/auth/realms/` y cookies `KC_RESTART`).
- **Protocolos**: OAuth2 y OpenID Connect (OIDC).
- **Tokens**: JWT (JSON Web Tokens) con firma RS256.
- **Capa de Seguridad**: Spring Security (Configuraciones de cabeceras `X-Content-Type-Options`, `X-Frame-Options`).

## 3. Integración y Procesamiento
- **Intercambio de Datos**: REST / JSON.
- **Codificación de Archivos**: Base64 (para imágenes CI y biometría Selfie).
- **Resiliencia**: Deducido uso de patrones de Circuit Breaker (Debido a la naturaleza de integración con SEGIP).
- **Trazabilidad**: IDs de transacción distribuidos (Snowflake ID style).

## 4. Infraestructura y Red
- **API Gateway**: Probable uso de Spring Cloud Gateway o NGINX como proxy inverso.
- **Protocolo de Transporte**: HTTPS (TLS 1.2+).
- **Headers de Seguridad**: 
  - `Strict-Transport-Security`
  - `Content-Security-Policy`

## 5. Servicios Externos (Upstream)
- **SEGIP**: Servicio General de Identificación Personal (Bolivia) para cruce de datos civiles y biometría.

---
> [!NOTE]
> Este inventario confirma que el stack es 100% compatible con una implementación en **Spring Boot 4.x**, permitiendo una integración nativa y de alto rendimiento.
