# Integración de API Bancaria: Identidad y Firma v3

Este plan describe los pasos para integrar la API "Identidad y Firma v3" en un backend de Spring Boot 4.x, garantizando alta disponibilidad, seguridad y observabilidad.

## Cambios Propuestos

### Documentación y Especificación
- [NUEVO] `api_specification.md`: Tabla completa de todos los endpoints descubiertos.
- [NUEVO] `openapi.yaml`: Especificación OpenAPI 3.0 para la API.

### Implementación Backend (Spring Boot 4.x / Java 21)

#### Fundación y Configuración
- [NUEVO] `application.yml`: Configuración para Keycloak (auth), URLs base de la API y timeouts.
- [NUEVO] `SecurityConfig.java`: Configuración del cliente OAuth2 e interceptores JWT.

#### Modelos de Dominio (DTOs)
- [NUEVO] `IdentityRecords.java`: Java 21 records para solicitudes/respuestas de OCR y validación de identidad.

#### Capa de Cliente API
- [NUEVO] `WebClientConfig.java`: Configuración de WebClient reactivo con registro y encabezados personalizados.
- [NUEVO] `IdentityClient.java`: Implementación del consumidor de API usando WebClient y Resilience4j (Circuit Breaker, Retry).

#### Capa de Servicio y Lógica
- [NUEVO] `IdentityService.java`: Lógica de negocio para el onboarding, manejando la transformación entre modelos internos y externos.

#### Observabilidad
- [NUEVO] `ObservationConfig.java`: Integración con Micrometer y OpenTelemetry para trazabilidad.
- [NUEVO] `StructuredLogging.java`: Configuración de Logback para registros estructurados en JSON.

## Plan de Verificación

### Pruebas Automatizadas
- **Pruebas Unitarias**: Probar la serialización/deserialización de DTOs y la lógica del servicio usando JUnit 5 y AssertJ.
  - Ejecutar: `mvn test`
- **Pruebas de Integración**: Verificar el cliente API contra un servidor simulado (WireMock).
  - Ejecutar: `mvn verify -Pintegration-test`

### Verificación Manual
- Verificar la especificación OpenAPI generada en Swagger Editor.
- Inspeccionar los logs para asegurar que no se filtren datos sensibles (imágenes Base64).
- Validar la propagación de `X-Correlation-Id` entre servicios internos y llamadas API externas.
