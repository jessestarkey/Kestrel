The mission teams' dev, test, and stage clusters will run on synthetic or sanitized data, never live mission data. Each set is sanitized inside its own team's zone, so the payload vendor split holds, and then reaches that team's dev/test spoke over F23. Presidio removes identifying text.

People in imagery need more care. Until the person-detection model is certified in Phase 3, a Data Team reviewer blurs or crops people by hand. After that, the model runs as a batch job in each zone's sanitizing pipeline.
