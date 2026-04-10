# Evaluación de Riesgos de Seguridad: Identidad y Firma v3 (Estándares Bancarios)

## Riesgos Identificados

### 1. Exposición de PII Sensible y Datos Biométricos (OWASP A03:2021)
- **Riesgo**: Los cuerpos de solicitud para `getOCR` y `createdoubleidentity` contienen cadenas Base64 de cédulas de identidad y selfies.
- **Impacto**: El registro accidental en logs o la interceptación podría conducir al robo de identidad.
- **Mitigación**: 
  - Implementación de **Enmascaramiento de Datos** en todos los interceptores de registro.
  - **Cifrado a nivel de campo** estricto para PII en tránsito cuando corresponda.

### 2. Dependencia de Proveedores de Identidad Externos (SEGIP)
- **Riesgo**: La disponibilidad del sistema depende de una base de datos estatal.
- **Impacto**: La latencia o las interrupciones en SEGIP podrían interrumpir el proceso de onboarding bancario.
- **Mitigación**:
  - Implementación de **Circuit Breakers (Resilience4j)** para fallar rápido y proporcionar alternativas significativas.
  - **Procesamiento asíncrono** para pasos de onboarding no bloqueantes.

### 3. Falta de Limitación de Tasa y Vulnerabilidad de DoS
- **Riesgo**: Los endpoints de la API consumen muchos recursos (procesamiento de OCR/biométrico).
- **Impacto**: Actores maliciosos podrían agotar los recursos.
- **Mitigación**:
  - Implementar **Limitación de Tasa** en el nivel del API Gateway (ej. Spring Cloud Gateway).
  - Usar un **Web Application Firewall (WAF)** para el filtrado de solicitudes.

## Controles de Seguridad Propuestos (Nivel Bancario)

- **Arquitectura Zero Trust**: Sin confianza implícita. Validar ámbitos (scopes) y roles de JWT en cada llamada interna.
- **Mutual TLS (mTLS)**: Aplicar autenticación basada en certificados entre el backend de Spring Boot y los microservicios de identidad.
- **JSON Web Encryption (JWE)**: Cifrar payloads sensibles usando pares de claves pública/privada si los datos necesitan ser almacenados temporalmente en caché.
- **Trazabilidad**: `X-Correlation-ID` obligatorio para cada transacción para garantizar la auditabilidad de extremo a extremo.
- **Auditoría**: Registrar cada evento de autenticación y transición de estado (Borrador -> Pendiente -> Validado).
