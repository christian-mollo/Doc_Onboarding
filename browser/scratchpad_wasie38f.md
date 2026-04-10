# API Tech Stack Inventory - Final

## Identified Technologies
1. **Authentication / IAM**: **Keycloak (v10.0+)**
   - **Evidence**: 
     - Authentication URL: `{{BASIC__URL}}/auth/realms/digital_identity/protocol/openid-connect/token`.
     - Cookie names: `KEYCLOAK_LOCALE`, `KC_RESTART`.
     - Explicit link to Keycloak JavaDocs in the `GetToken` note: `https://www.keycloak.org/docs-api/10.0/javadocs/...`.
2. **Protocol**: **OpenID Connect / OAuth2**
   - **Evidence**: Standard usage of `grant_type=password`, `client_id`, `client_secret`, `access_token`, `refresh_token`.
3. **Backend Framework**: **Java / Spring Boot**
   - **Evidence**:
     - Standard identity management integration (Keycloak + Spring Boot).
     - Response headers such as `X-Frame-Options: SAMEORIGIN`, `X-XSS-Protection: 1; mode=block`, and `Cache-Control: no-cache, no-store, max-age=0, must-revalidate` are default Spring Security configurations.
     - Microservices naming convention (`ms-digital-identity-profirma`).
     - JSON structure with a standard `status` object (code, message, timestamp, transactionId) common in enterprise Spring applications.
4. **Architecture**: **Microservices**
   - **Evidence**: Endpoint path pattern `/api/ms-[service-name]/...`.
5. **ID Generation**: **Distributed ID (Snowflake or similar)**
   - **Evidence**: Use of long numeric `transactionId`.
6. **Infrastructure & DevOps**:
   - Environment-based configuration (variables `BASIC_URL`, `BASIC__URL`).
   - Security headers suggest the presence of an **API Gateway** or **Ingress Controller** (e.g., Spring Cloud Gateway or NGINX).
7. **Business Domain**: **Fintech / KYC / Digital Identity**
   - Specific modules for SEGIP validation (Bolivian Govt) and OCR document reading.

## Observations
- No specific database is mentioned, but typical enterprise Spring Boot setups use **PostgreSQL** or **Oracle**.
- The use of Keycloak 10.0 suggests a stable enterprise environment, though possibly not the bleeding edge version.
- API follows RESTful principles with strong emphasis on security and auditability (transaction IDs).