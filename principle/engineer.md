# Engineering Standards

## 1. Core Architecture Goals
- **Simple & Practical:** Solve the immediate problem; avoid over-engineering.
- **Low Coupling & High Cohesion:** Minimize inter-module dependencies; focus on single-purpose components.
- **Extensible & Flexible:** Design for future logic injection without modifying the core.
- **Orthogonal:** Ensure changes in one module have zero side effects on others.
- **Robust & Resilient:** Implement graceful error handling and self-healing.
- **Evolutionary:** Allow the system to grow iteratively from a simple base.
- **Testable:** Decouple logic from infrastructure to ensure high testability.

## 2. Mandatory Principles
- **SOLID:** Strictly follow SRP, OCP, LSP, ISP, and DIP.
- **DRY:** Zero tolerance for logic redundancy.
- **KISS:** Prioritize readability and direct implementation.
- **YAGNI:** Do not implement features for "future" hypothetical scenarios.
- **MVP:** Deliver functional, minimal logic first, then refactor for performance.

## 3. Implementation Checklist
1. Is this the simplest yet effective way to achieve the goal?
2. If I change this function, will it break unrelated modules?
3. Can this logic be unit-tested without complex mocks?
4. Are errors handled or just suppressed?