# Archangel 1.7.0a6 - Channels and shared-note receipts

This engineering alpha extends the exact 1.7.0a5 Mac-Launcher-Fix1 source baseline. It is not a website, Stripe, relay or public-download update.

## Added

- Signed, stable channel descriptors and signed channel-note metadata bound to capsule content. Channel names alone are not identities.
- Receiver-local Send to / Receive from / Use in chat permissions, versioned policy edits, explicit archive and outgoing pause controls, signed channel-card import/export.
- A persistent channel Chat view, local model choice, bounded conversation history, current-scope field retrieval, conflict-aware guarded completion, and expandable source receipts.
- Shared-note counts derived from unique exact atoms actually supplied to the completion request; includes conflict supplements and historical grounding, never search candidates. Full generation branch, context hash and source records remain inspectable.
- Reviewed local channel notes with local Phase B commit and per-destination durable outcomes. Existing unknown-receipt locks stay intact.
- Literal phrase-based draft suggestions and double-opt-in automatic /note messages from the current local user conversation, with durable event deduplication, rate limits, no incoming/model-output forwarding, and no restart replay.
- Signed-note file export/import, an offline QR reel exporter, and channel-aware intake after retained optical chunk reconstruction. Direct sends require refreshed a6-capable rig cards.
- a6-aware desktop/trust snapshot even when an a5 migration marker already exists. Mac runtime discovery fix retained. No new third-party Python dependency.

## Retained

Inbox/Sent/Drafts, reviewed summary composer, direct mutual TLS and approved identity binding, strict receiver commit boundary, field persistence, replay controls, numerical/route validation, exact source preservation, conflict guarding, retained Advanced workspace/CLI, isolated/default and explicit offline/host runtime paths.

## Boundaries

Normal chat integration is inside Archangel, not an automatic hook into unrelated apps. Embeddings select explicit text evidence, not universal latent/weights/KV-cache transfer. Channels are logical views and local policy over the existing field, not new model coordinate systems. Automatic topic inference, free-running agents, production channel-aware Managed Relay, native signed installers, formal conflict-resolution authoring and physical cross-platform/camera validation are not asserted complete.

Public website/download and existing working a5 rigs are untouched by preparing this release. Test the same a6 wheel on both rigs before promotion.
