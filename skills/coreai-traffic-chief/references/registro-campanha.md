# Registro local (fora das skills)
Usar businesses/<slug>/outputs/campanhas/<campanha>/ na raiz ContextOS escolhida (validado antes por coreai-shared/scripts/gate.py --root <raiz> --business <slug> --output <destino-absoluto>), se salvamento autorizado. Não sobrescrever registros anteriores.

campaign-brief.md: negócio, produto, fontes, objetivo, destino, público, copy/imagem, conta ID/nome, moeda, tipo/verba/período, medição, decisões, lacunas.
tracking-review.md: aplicabilidade, evento/ativo, fonte observada/data, limitações.
review.md: revisão interna, itens aprovados/reprovados, responsável e horário.
actions.jsonl: registros append-only com operation_id, timestamp, ação, conta, estado planned/pending/success/failed/unknown, IDs retornados e verificação; nunca token/headers segredos.
manifest.json: campaign_id, adset_ids, ad_ids, estado desejado PAUSED, estados observados, checked_at, arquivos/recibos, pendências. Não inventar identificadores.

Sem criação externa, o manifesto deve dizer NOT_CREATED e IDs ausentes. Aprovação interna, criação, revisão Meta e veiculação são fatos diferentes.
