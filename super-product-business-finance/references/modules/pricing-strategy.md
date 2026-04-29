## Module: Pricing Strategy
---
name: pricing-strategy
description: "Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Pricing Strategy

You are an expert in pricing and monetization strategy. Your goal is to help design pricing that **captures value, supports growth, and aligns with customer willingness to pay**—without harming conversion, trust, or long-term retention.

This skill covers **pricing research, value metrics, tier design, and pricing change strategy**.
It does **not** implement pricing pages or experiments directly.

---

## 1. Required Context (Ask If Missing)

### 1. Business Model

* Product type (SaaS, marketplace, service, usage-based)
* Current pricing (if any)
* Target customer (SMB, mid-market, enterprise)
* Go-to-market motion (self-serve, sales-led, hybrid)

### 2. Market & Competition

* Primary value delivered
* Key alternatives customers compare against
* Competitor pricing models
* Differentiation vs. alternatives

### 3. Current Performance (If Existing)

* Conversion rate
* ARPU / ARR
* Churn and expansion
* Qualitative pricing feedback

### 4. Objectives

* Growth vs. revenue vs. profitability
* Move upmarket or downmarket
* Planned pricing changes (if any)

---

## 2. Pricing Fundamentals

### The Three Pricing Decisions

Every pricing strategy must explicitly answer:

1. **Packaging** – What is included in each tier?
2. **Value Metric** – What customers pay for (users, usage, outcomes)?
3. **Price Level** – How much each tier costs

Failure in any one weakens the system.

---

## 3. Value-Based Pricing Framework

Pricing should be anchored to **customer-perceived value**, not internal cost.

```
Customer perceived value
───────────────────────────────
Your price
───────────────────────────────
Next best alternative
───────────────────────────────
Your cost to serve
```

**Rules**

* Price above the next best alternative
* Leave customer surplus (value they keep)
* Cost is a floor, not a pricing basis

---

## 4. Pricing Research Methods

### Van Westendorp (Price Sensitivity Meter)

Used to identify acceptable price ranges.

**Questions**

* Too expensive
* Too cheap
* Expensive but acceptable
* Cheap / good value

**Key Outputs**

* PMC (too cheap threshold)
* PME (too expensive threshold)
* OPP (optimal price point)
* IDP (indifference price point)

**Use Case**

* Early pricing
* Price increase validation
* Segment comparison

---

### Feature Value Research (MaxDiff / Conjoint)

Used to inform **packaging**, not price levels.

**Insights Produced**

* Table-stakes features
* Differentiators
* Premium-only features
* Low-value candidates to remove

---

### Willingness-to-Pay Testing

| Method        | Use Case                    |
| ------------- | --------------------------- |
| Direct WTP    | Directional only            |
| Gabor-Granger | Demand curve                |
| Conjoint      | Feature + price sensitivity |

---

## 5. Value Metrics

### Definition

The value metric is **what scales price with customer value**.

### Good Value Metrics

* Align with value delivered
* Scale with customer success
* Easy to understand
* Difficult to game

### Common Patterns

| Metric             | Best For             |
| ------------------ | -------------------- |
| Per user           | Collaboration tools  |
| Per usage          | APIs, infrastructure |
| Per record/contact | CRMs, email          |
| Flat fee           | Simple products      |
| Revenue share      | Marketplaces         |

### Validation Test

> As customers get more value, do they naturally pay more?

If not → metric is misaligned.

---

## 6. Tier Design

### Number of Tiers

| Count | When to Use                    |
| ----- | ------------------------------ |
| 2     | Simple segmentation            |
| 3     | Default (Good / Better / Best) |
| 4+    | Broad market, careful UX       |

### Good / Better / Best

**Good**

* Entry point
* Limited usage
* Removes friction

**Better (Anchor)**

* Where most customers should land
* Full core value
* Best value-per-dollar

**Best**

* Power users / enterprise
* Advanced controls, scale, support

---

### Differentiation Levers

* Usage limits
* Advanced features
* Support level
* Security & compliance
* Customization / integrations

---

## 7. Persona-Based Packaging

### Step 1: Define Personas

Segment by:

* Company size
* Use case
* Sophistication
* Budget norms

### Step 2: Map Value to Tiers

Ensure each persona clearly maps to *one* tier.

### Step 3: Price to Segment WTP

Avoid “one price fits all” across fundamentally different buyers.

---

## 8. Freemium vs. Free Trial

### Freemium Works When

* Large market
* Viral or network effects
* Clear upgrade trigger
* Low marginal cost

### Free Trial Works When

* Value requires setup
* Higher price points
* B2B evaluation cycles
* Sticky post-activation usage

### Hybrid Models

* Reverse trials
* Feature-limited free + premium trial

---

## 9. Price Increases

### Signals It’s Time

* Very high conversion
* Low churn
* Customers under-paying relative to value
* Market price movement

### Increase Strategies

1. New customers only
2. Delayed increase for existing
3. Value-tied increase
4. Full plan restructure

---

## 10. Pricing Page Alignment (Strategy Only)

This skill defines **what** pricing should be.
Execution belongs to **page-cro**.

Strategic requirements:

* Clear recommended tier
* Transparent differentiation
* Annual discount logic
* Enterprise escape hatch

---

## 11. Price Testing (Safe Methods)

Preferred:

* New-customer pricing
* Sales-led experimentation
* Geographic tests
* Packaging tests

Avoid:

* Blind A/B price tests on same page
* Surprise customer discovery

---

## 12. Enterprise Pricing

### When to Introduce

* Deals > $10k ARR
* Custom contracts
* Security/compliance needs
* Sales involvement required

### Common Structures

* Volume-discounted per seat
* Platform fee + usage
* Outcome-based pricing

---

## 13. Output Expectations

This skill produces:

### Pricing Strategy Document

* Target personas
* Value metric selection
* Tier structure
* Price rationale
* Research inputs
* Risks & tradeoffs

### Change Recommendation (If Applicable)

* Who is affected
* Expected impact
* Rollout plan
* Measurement plan

---

## 14. Validation Checklist

* [ ] Clear value metric
* [ ] Distinct tier personas
* [ ] Research-backed price range
* [ ] Conversion-safe entry tier
* [ ] Expansion path exists
* [ ] Enterprise handled explicitly

---
Related Skills

page-cro – Pricing page conversion

copywriting – Pricing copy

analytics-tracking – Measure impact

ab-test-setup – Safe experimentation

marketing-psychology – Behavioral pricing effects

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Imported Reference

---
name: monetization
description: Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e modelos de negocio...
risk: none
source: community
date_added: '2026-03-06'
author: renat
tags:
- monetization
- stripe
- saas
- pricing
- subscriptions
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# MONETIZATION - Do Produto ao Revenue

## Overview

Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e modelos de negocio SaaS. Ativar para: integrar Stripe, criar planos de assinatura, pricing strategy, upgrade/downgrade, webhook de pagamento, trial gratuito, churn, LTV/CAC, unit economics, modelo de negocio.

## When to Use This Skill

- When you need specialized assistance with this domain

## Do Not Use This Skill When

- The task is unrelated to monetization
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

> Price is what you pay. Value is what you get. - Warren Buffett
> A monetizacao perfeita captura valor proporcional ao valor entregue.

---

## A Regra De Ouro

Usuarios pagam quando:
1. O produto resolve um problema real (need)
2. A solucao e melhor que alternativas (differentiation)
3. O preco e percebido como justo (value perception)
4. O momento de cobranca e natural (timing)

## Erros Classicos

- Cobranca antes de mostrar valor (kill activation)
- Preco muito baixo (sinaliza baixa qualidade)
- Planos demais (paralisia de escolha)
- Trial sem carta de credito (baixa conversao)
- Churn invisivel (sem alertas de cancelamento iminente)

---

## Setup Inicial

```bash
pip install stripe

## Ou

npm install stripe
```

```python

## Config.Py

import stripe
import os

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
STRIPE_WEBHOOK_SECRET = os.environ["STRIPE_WEBHOOK_SECRET"]

PLANS = {
    "free": None,
    "pro": os.environ["STRIPE_PRICE_PRO"],
    "business": os.environ["STRIPE_PRICE_BIZ"],
}
```

## Criar Customer E Subscription

```python
def create_customer(email: str, name: str, user_id: str) -> str:
    customer = stripe.Customer.create(
        email=email,
        name=name,
        metadata={"user_id": user_id}
    )
    return customer.id

def create_subscription(customer_id: str, price_id: str, trial_days: int = 14):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[{"price": price_id}],
        trial_period_days=trial_days,
        payment_behavior="default_incomplete",
        expand=["latest_invoice.payment_intent"],
    )
    return {
        "subscription_id": subscription.id,
        "client_secret": subscription.latest_invoice.payment_intent.client_secret,
        "status": subscription.status
    }
```

## Checkout Session (Recomendado Para Conversao)

```python
def create_checkout_session(
    customer_id: str,
    price_id: str,
    success_url: str,
    cancel_url: str,
    trial_days: int = 14
) -> str:
    session = stripe.checkout.Session.create(
        customer=customer_id,
        mode="subscription",
        line_items=[{"price": price_id, "quantity": 1}],
        subscription_data={"trial_period_days": trial_days},
        success_url=success_url + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=cancel_url,
        allow_promotion_codes=True,
    )
    return session.url
```

## Customer Portal (Self-Service)

```python
def create_portal_session(customer_id: str, return_url: str) -> str:
    session = stripe.billing_portal.Session.create(
        customer=customer_id,
        return_url=return_url,
    )
    return session.url
```

## Webhook - Processar Eventos

```python
from fastapi import Request, HTTPException
import stripe

async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    handlers = {
        "customer.subscription.created": handle_subscription_created,
        "customer.subscription.updated": handle_subscription_updated,
        "customer.subscription.deleted": handle_subscription_deleted,
        "invoice.payment_succeeded": handle_payment_succeeded,
        "invoice.payment_failed": handle_payment_failed,
        "customer.subscription.trial_will_end": handle_trial_ending,
    }

    handler = handlers.get(event["type"])
    if handler:
        await handler(event["data"]["object"])

    return {"status": "ok"}
```

## Verificar Status Da Subscription

```python
def get_subscription_status(customer_id: str) -> dict:
    subscriptions = stripe.Subscription.list(
        customer=customer_id,
        status="all",
        limit=1
    )
    if not subscriptions.data:
        return {"tier": "free", "status": "none"}

    sub = subscriptions.data[0]
    return {
        "tier": get_tier_from_price(sub.items.data[0].price.id),
        "status": sub.status,
        "trial_end": sub.trial_end,
        "current_period_end": sub.current_period_end,
        "cancel_at_period_end": sub.cancel_at_period_end,
    }
```

---

## Framework De Pricing Para Saas

**Metodo 1: Value-Based Pricing (Recomendado)**
```
1. Calcule o valor economico entregue ao usuario
   Ex: produto economiza 2h/semana = R$ 200/mes de valor
2. Capture 10-30% do valor criado
   Ex: R$ 29/mes = 14% do valor
3. Valide com pesquisa de willingness-to-pay
4. Teste 3 price points (A/B test)
```

**Metodo 2: Competitive Anchor**
```
Referencia: ChatGPT Plus = $20/mes (R$ 100)
Anchor: Notion = R$ 32/mes
Posicao: Pro = R$ 29/mes (mais barato que ChatGPT, similar ao Notion)
Mensagem: Tudo que o ChatGPT faz, por voz no Alexa
```

## Psicologia De Pricing

```
R$ 29/mes (nao R$ 30 - efeito do digito esquerdo)
Plano anual com desconto claro: R$ 249/ano (economize R$ 99)
Destaque no plano que voce quer vender (visual hierarchy)
Ancoragem: mostra o plano caro primeiro
Trial sem cartao para ativacao, com cartao para retencao
Badge Mais popular no plano middle
```

## Estrutura De Planos (3 E O Numero Certo)

| Feature             | Free    | Pro        | Business   |
|---------------------|---------|------------|------------|
| Preco               | Gratis  | R$ 29/mes  | R$ 99/mes  |
| Conversas/mes       | 50      | Ilimitado  | Ilimitado  |
| Memoria             | 7 dias  | 1 ano      | Permanente |
| Board especialistas | Nao     | Sim        | Sim        |
| Multi-usuarios      | Nao     | Nao        | Ate 10     |
| API access          | Nao     | Nao        | Sim        |
| Suporte             | Nao     | Email      | Priority   |

---

## Sinais De Churn Iminente

```python
CHURN_SIGNALS = {
    "high_risk": [
        "nao logou nos ultimos 14 dias",
        "uso caiu >70% em 2 semanas",
        "abriu cancelamento mas nao concluiu",
        "ticket de suporte aberto sem resolucao",
    ],
    "medium_risk": [
        "nao logou em 7 dias",
        "uso caiu >40%",
        "nao completou onboarding",
        "nunca usou feature core",
    ]
}
```

## Sequencia Anti-Churn

```
Dia 0:  Usuario nao usa por 7 dias
        -> Email: Sentimos sua falta. O que aconteceu?

Dia 3:  Sem resposta
        -> Push/Email: case study de usuario similar com sucesso

Dia 7:  Nao voltou
        -> Email: oferta especial (20% off por 3 meses)

Dia 14: Trial expirando
        -> In-app modal + email urgente: Sua conta vai dormir em 3 dias

Dia 30: Cancelou
        -> Offboarding email: Lamentamos ver voce ir.
        -> 3 meses depois: reativacao com novidades
```

## Exit Survey (Obrigatorio)

```python
CANCELLATION_REASONS = [
    "Muito caro",
    "Nao uso o suficiente",
    "Falta funcionalidade X",
    "Encontrei alternativa melhor",
    "Problemas tecnicos",
    "Outro"
]

## Falta Feature -> Roadmap + Notificacao Quando Lancar

```

---

## Calculos Essenciais

```python
def calculate_unit_economics(
    mrr: float,
    customers: int,
    new_customers: int,
    churned: int,
    cac_total: float,
):
    arpu = mrr / customers
    churn_rate = churned / customers
    ltv = arpu / churn_rate
    cac = cac_total / new_customers
    ltv_cac = ltv / cac
    months_to_recover_cac = cac / arpu

    return {
        "ARPU": f"R$ {arpu:.2f}",
        "Churn Rate": f"{churn_rate*100:.1f}%",
        "LTV": f"R$ {ltv:.0f}",
        "CAC": f"R$ {cac:.0f}",
        "LTV/CAC": f"{ltv_cac:.1f}x",
        "Payback": f"{months_to_recover_cac:.1f} meses",
        "Status": "Saudavel" if ltv_cac > 3 else "Otimizar"
    }
```

## Benchmarks Saas B2C Brasil

| Metrica               | Ruim  | Ok     | Bom    | Excelente |
|-----------------------|-------|--------|--------|-----------|
| Churn Mensal          | >7%   | 5-7%   | 2-5%   | <2%       |
| LTV/CAC               | <1x   | 1-3x   | 3-5x   | >5x       |
| Payback               | >18m  | 12-18m | 6-12m  | <6m       |
| Conversao trial->pago | <3%   | 3-8%   | 8-15%  | >15%      |
| MoM Growth            | <5%   | 5-10%  | 10-20% | >20%      |

---

## Dashboard De Revenue (Metricas Diarias)

```
MRR atual: R$ XX.XXX
  New MRR (novos assinantes): +R$ X.XXX
  Expansion MRR (upgrades): +R$ XXX
  Contraction MRR (downgrades): -R$ XXX
  Churned MRR (cancelamentos): -R$ XXX
  Net New MRR: +/- R$ XXX

ARR (Annualized): R$ XX.XXX x 12
Churn Rate: X.X%
Net Revenue Retention: XXX% (meta: >100%)
```

## Automacao De Revenue Com Stripe

```python
async def check_usage_and_upsell(user_id: str, usage: dict):
    if usage["conversations_this_month"] >= 45:
        await send_upgrade_prompt(
            user_id=user_id,
            message="Voce esta usando 90% do seu limite. Faca upgrade para Pro.",
            cta_url=f"/upgrade?utm=usage-limit"
        )
```

---

## 7. Comandos Rapidos

| Comando              | Acao                                     |
|----------------------|------------------------------------------|
| /stripe-setup        | Configura Stripe do zero                 |
| /pricing-analysis    | Analisa estrategia de pricing atual      |
| /churn-playbook      | Sequencia anti-churn personalizada       |
| /unit-economics      | Calcula LTV/CAC e saude financeira       |
| /upgrade-flow        | Design do fluxo de upgrade               |
| /revenue-dashboard   | Template de dashboard de revenue         |
| /trial-optimization  | Otimiza conversao de trial               |

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `analytics-product` - Complementary skill for enhanced analysis
- `growth-engine` - Complementary skill for enhanced analysis
- `product-design` - Complementary skill for enhanced analysis
- `product-inventor` - Complementary skill for enhanced analysis

## Imported Module: Monetization
---
name: monetization
description: Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e modelos de negocio...
risk: none
source: community
date_added: '2026-03-06'
author: renat
tags:
- monetization
- stripe
- saas
- pricing
- subscriptions
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# MONETIZATION - Do Produto ao Revenue

## Overview

Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e modelos de negocio SaaS. Ativar para: integrar Stripe, criar planos de assinatura, pricing strategy, upgrade/downgrade, webhook de pagamento, trial gratuito, churn, LTV/CAC, unit economics, modelo de negocio.

## When to Use This Skill

- When you need specialized assistance with this domain

## Do Not Use This Skill When

- The task is unrelated to monetization
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

> Price is what you pay. Value is what you get. - Warren Buffett
> A monetizacao perfeita captura valor proporcional ao valor entregue.

---

## A Regra De Ouro

Usuarios pagam quando:
1. O produto resolve um problema real (need)
2. A solucao e melhor que alternativas (differentiation)
3. O preco e percebido como justo (value perception)
4. O momento de cobranca e natural (timing)

## Erros Classicos

- Cobranca antes de mostrar valor (kill activation)
- Preco muito baixo (sinaliza baixa qualidade)
- Planos demais (paralisia de escolha)
- Trial sem carta de credito (baixa conversao)
- Churn invisivel (sem alertas de cancelamento iminente)

---

## Setup Inicial

```bash
pip install stripe

## Ou

npm install stripe
```

```python

## Config.Py

import stripe
import os

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
STRIPE_WEBHOOK_SECRET = os.environ["STRIPE_WEBHOOK_SECRET"]

PLANS = {
    "free": None,
    "pro": os.environ["STRIPE_PRICE_PRO"],
    "business": os.environ["STRIPE_PRICE_BIZ"],
}
```

## Criar Customer E Subscription

```python
def create_customer(email: str, name: str, user_id: str) -> str:
    customer = stripe.Customer.create(
        email=email,
        name=name,
        metadata={"user_id": user_id}
    )
    return customer.id

def create_subscription(customer_id: str, price_id: str, trial_days: int = 14):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[{"price": price_id}],
        trial_period_days=trial_days,
        payment_behavior="default_incomplete",
        expand=["latest_invoice.payment_intent"],
    )
    return {
        "subscription_id": subscription.id,
        "client_secret": subscription.latest_invoice.payment_intent.client_secret,
        "status": subscription.status
    }
```

## Checkout Session (Recomendado Para Conversao)

```python
def create_checkout_session(
    customer_id: str,
    price_id: str,
    success_url: str,
    cancel_url: str,
    trial_days: int = 14
) -> str:
    session = stripe.checkout.Session.create(
        customer=customer_id,
        mode="subscription",
        line_items=[{"price": price_id, "quantity": 1}],
        subscription_data={"trial_period_days": trial_days},
        success_url=success_url + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=cancel_url,
        allow_promotion_codes=True,
    )
    return session.url
```

## Customer Portal (Self-Service)

```python
def create_portal_session(customer_id: str, return_url: str) -> str:
    session = stripe.billing_portal.Session.create(
        customer=customer_id,
        return_url=return_url,
    )
    return session.url
```

## Webhook - Processar Eventos

```python
from fastapi import Request, HTTPException
import stripe

async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    handlers = {
        "customer.subscription.created": handle_subscription_created,
        "customer.subscription.updated": handle_subscription_updated,
        "customer.subscription.deleted": handle_subscription_deleted,
        "invoice.payment_succeeded": handle_payment_succeeded,
        "invoice.payment_failed": handle_payment_failed,
        "customer.subscription.trial_will_end": handle_trial_ending,
    }

    handler = handlers.get(event["type"])
    if handler:
        await handler(event["data"]["object"])

    return {"status": "ok"}
```

## Verificar Status Da Subscription

```python
def get_subscription_status(customer_id: str) -> dict:
    subscriptions = stripe.Subscription.list(
        customer=customer_id,
        status="all",
        limit=1
    )
    if not subscriptions.data:
        return {"tier": "free", "status": "none"}

    sub = subscriptions.data[0]
    return {
        "tier": get_tier_from_price(sub.items.data[0].price.id),
        "status": sub.status,
        "trial_end": sub.trial_end,
        "current_period_end": sub.current_period_end,
        "cancel_at_period_end": sub.cancel_at_period_end,
    }
```

---

## Framework De Pricing Para Saas

**Metodo 1: Value-Based Pricing (Recomendado)**
```
1. Calcule o valor economico entregue ao usuario
   Ex: produto economiza 2h/semana = R$ 200/mes de valor
2. Capture 10-30% do valor criado
   Ex: R$ 29/mes = 14% do valor
3. Valide com pesquisa de willingness-to-pay
4. Teste 3 price points (A/B test)
```

**Metodo 2: Competitive Anchor**
```
Referencia: ChatGPT Plus = $20/mes (R$ 100)
Anchor: Notion = R$ 32/mes
Posicao: Pro = R$ 29/mes (mais barato que ChatGPT, similar ao Notion)
Mensagem: Tudo que o ChatGPT faz, por voz no Alexa
```

## Psicologia De Pricing

```
R$ 29/mes (nao R$ 30 - efeito do digito esquerdo)
Plano anual com desconto claro: R$ 249/ano (economize R$ 99)
Destaque no plano que voce quer vender (visual hierarchy)
Ancoragem: mostra o plano caro primeiro
Trial sem cartao para ativacao, com cartao para retencao
Badge Mais popular no plano middle
```

## Estrutura De Planos (3 E O Numero Certo)

| Feature             | Free    | Pro        | Business   |
|---------------------|---------|------------|------------|
| Preco               | Gratis  | R$ 29/mes  | R$ 99/mes  |
| Conversas/mes       | 50      | Ilimitado  | Ilimitado  |
| Memoria             | 7 dias  | 1 ano      | Permanente |
| Board especialistas | Nao     | Sim        | Sim        |
| Multi-usuarios      | Nao     | Nao        | Ate 10     |
| API access          | Nao     | Nao        | Sim        |
| Suporte             | Nao     | Email      | Priority   |

---

## Sinais De Churn Iminente

```python
CHURN_SIGNALS = {
    "high_risk": [
        "nao logou nos ultimos 14 dias",
        "uso caiu >70% em 2 semanas",
        "abriu cancelamento mas nao concluiu",
        "ticket de suporte aberto sem resolucao",
    ],
    "medium_risk": [
        "nao logou em 7 dias",
        "uso caiu >40%",
        "nao completou onboarding",
        "nunca usou feature core",
    ]
}
```

## Sequencia Anti-Churn

```
Dia 0:  Usuario nao usa por 7 dias
        -> Email: Sentimos sua falta. O que aconteceu?

Dia 3:  Sem resposta
        -> Push/Email: case study de usuario similar com sucesso

Dia 7:  Nao voltou
        -> Email: oferta especial (20% off por 3 meses)

Dia 14: Trial expirando
        -> In-app modal + email urgente: Sua conta vai dormir em 3 dias

Dia 30: Cancelou
        -> Offboarding email: Lamentamos ver voce ir.
        -> 3 meses depois: reativacao com novidades
```

## Exit Survey (Obrigatorio)

```python
CANCELLATION_REASONS = [
    "Muito caro",
    "Nao uso o suficiente",
    "Falta funcionalidade X",
    "Encontrei alternativa melhor",
    "Problemas tecnicos",
    "Outro"
]

## Falta Feature -> Roadmap + Notificacao Quando Lancar

```

---

## Calculos Essenciais

```python
def calculate_unit_economics(
    mrr: float,
    customers: int,
    new_customers: int,
    churned: int,
    cac_total: float,
):
    arpu = mrr / customers
    churn_rate = churned / customers
    ltv = arpu / churn_rate
    cac = cac_total / new_customers
    ltv_cac = ltv / cac
    months_to_recover_cac = cac / arpu

    return {
        "ARPU": f"R$ {arpu:.2f}",
        "Churn Rate": f"{churn_rate*100:.1f}%",
        "LTV": f"R$ {ltv:.0f}",
        "CAC": f"R$ {cac:.0f}",
        "LTV/CAC": f"{ltv_cac:.1f}x",
        "Payback": f"{months_to_recover_cac:.1f} meses",
        "Status": "Saudavel" if ltv_cac > 3 else "Otimizar"
    }
```

## Benchmarks Saas B2C Brasil

| Metrica               | Ruim  | Ok     | Bom    | Excelente |
|-----------------------|-------|--------|--------|-----------|
| Churn Mensal          | >7%   | 5-7%   | 2-5%   | <2%       |
| LTV/CAC               | <1x   | 1-3x   | 3-5x   | >5x       |
| Payback               | >18m  | 12-18m | 6-12m  | <6m       |
| Conversao trial->pago | <3%   | 3-8%   | 8-15%  | >15%      |
| MoM Growth            | <5%   | 5-10%  | 10-20% | >20%      |

---

## Dashboard De Revenue (Metricas Diarias)

```
MRR atual: R$ XX.XXX
  New MRR (novos assinantes): +R$ X.XXX
  Expansion MRR (upgrades): +R$ XXX
  Contraction MRR (downgrades): -R$ XXX
  Churned MRR (cancelamentos): -R$ XXX
  Net New MRR: +/- R$ XXX

ARR (Annualized): R$ XX.XXX x 12
Churn Rate: X.X%
Net Revenue Retention: XXX% (meta: >100%)
```

## Automacao De Revenue Com Stripe

```python
async def check_usage_and_upsell(user_id: str, usage: dict):
    if usage["conversations_this_month"] >= 45:
        await send_upgrade_prompt(
            user_id=user_id,
            message="Voce esta usando 90% do seu limite. Faca upgrade para Pro.",
            cta_url=f"/upgrade?utm=usage-limit"
        )
```

---

## 7. Comandos Rapidos

| Comando              | Acao                                     |
|----------------------|------------------------------------------|
| /stripe-setup        | Configura Stripe do zero                 |
| /pricing-analysis    | Analisa estrategia de pricing atual      |
| /churn-playbook      | Sequencia anti-churn personalizada       |
| /unit-economics      | Calcula LTV/CAC e saude financeira       |
| /upgrade-flow        | Design do fluxo de upgrade               |
| /revenue-dashboard   | Template de dashboard de revenue         |
| /trial-optimization  | Otimiza conversao de trial               |

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `analytics-product` - Complementary skill for enhanced analysis
- `growth-engine` - Complementary skill for enhanced analysis
- `product-design` - Complementary skill for enhanced analysis
- `product-inventor` - Complementary skill for enhanced analysis

