# Reglas y Competencias de Desarrollo: Identidad y Firma v3

Para garantizar una implementación robusta, escalable y libre de errores en un entorno bancario de alta criticidad, se establecen las siguientes reglas mandatorias para el equipo de desarrollo.

## 1. Reglas Sugeridas para el Procesamiento de Datos
- **Fuerza Bruta de Formato (Mayúsculas)**: Es obligatorio implementar un interceptor de serialización o un componente de pre-procesamiento que asegure que todos los campos de texto (nombres, apellidos, direcciones) se envíen en **MAYÚSCULAS** a la API externa. 
  - *Excepciones*: `email`, `selfieFormat`, `obverseFormat`, `reverseFormat`.
- **Validación en el Límite**: Utilizar `Jakarta Validation` (Bean Validation 3.0) en todos los DTOs para fallar rápido antes de intentar cualquier llamada de red.

## 2. Competencias Técnicas y Arquitectónicas
- **Aislamiento de Errores (ACL)**: El backend actúa como una **Capa Anti-Corrupción (ACL)**. No se deben propagar los errores técnicos de la API externa (ej. stack traces de Jackson del OCR) tal cual vienen. Se deben mapear a un catálogo de errores bancarios internos.
- **Gestión Reactiva de Sesiones**: Implementar la renovación automática del token utilizando el `refresh_token` provisto. No se permite el almacenamiento de credenciales de usuario en sesión de larga duración.
- **Resiliencia Configurativa**:
  - `ConnectTimeout`: 5 segundos.
  - `ReadTimeout`: 30 segundos (debido al procesamiento pesado de imágenes).
  - `CircuitBreaker`: Configurar umbrales de fallo del 50% en una ventana de 10 llamadas para el servicio de OCR.

## 3. Seguridad y Auditoría
- **Enmascaramiento de PII**: Queda estrictamente prohibido registrar en logs los campos que contienen imágenes Base64 o datos de la biografía personal. Se debe utilizar una política de `Custom Masking` en Logback.
- **Propagación de Trazabilidad**: El `X-Correlation-ID` debe ser obligatorio y persistente a través de todo el flujo: `Login -> OCR -> Registro -> Firma`.
- **Inyección Alterna de Secretos**: Los valores sensibles (`client_secret`) deben manejarse exclusivamente a través de variables de entorno cifradas o un gestor de secretos (Vault/Secrets Manager).

## 4. Estándares de Código
- **Java Records**: Utilizar `Records` de Java 21 para todos los DTOs de transferencia para asegurar la inmutabilidad de los datos.
- **WebClient sobre RestTemplate**: Se prohíbe el uso de RestTemplate (bloqueante). Toda comunicación externa debe ser no-bloqueante y reactiva.
