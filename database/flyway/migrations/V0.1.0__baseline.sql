-- Создаём отдельную роль для приложения (на будущее)
CREATE ROLE biomachine_app LOGIN PASSWORD 'app_password';

-- Минимальные права
GRANT CONNECT ON DATABASE biomachine TO biomachine_app;

