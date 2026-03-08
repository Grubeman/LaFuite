# Résolution du problème CORS

## Changements effectués

### 1. Configuration du proxy Vite (`vite.config.js`)
- Ajout d'un proxy pour rediriger les requêtes `/api` vers `http://127.0.0.1:8000`
- Cela évite les problèmes CORS en développement car les requêtes passent par le même domaine

### 2. Mise à jour de l'URL de l'API (`.env`)
- Changement de `VITE_API_URL = "http://127.0.0.1:8000"` à `VITE_API_URL = ""`
- Les requêtes utiliseront maintenant le proxy local au lieu d'appeler directement le backend

### 3. NavBar avec authentification (`components/NavBar.jsx`)
- Affiche le nom d'utilisateur connecté à droite de la barre de navigation
- Affiche un bouton "Login" si aucun utilisateur n'est connecté
- Affiche un bouton "Déconnexion" si un utilisateur est connecté

## Important

### Pour le développement
Les changements ci-dessus fonctionnent pour le développement local. Le proxy Vite redirige automatiquement les requêtes.

### Pour la production
Pour la production, vous devez configurer CORS sur votre backend Django :

1. Installer `django-cors-headers`:
   ```bash
   pip install django-cors-headers
   ```

2. Ajouter à `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'corsheaders',
       ...
   ]

   MIDDLEWARE = [
       'corsheaders.middleware.CorsMiddleware',
       'django.middleware.common.CommonMiddleware',
       ...
   ]

   # Pour le développement
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:5173",
       "http://127.0.0.1:5173",
   ]

   # Pour la production (à adapter)
   # CORS_ALLOWED_ORIGINS = [
   #     "https://votre-domaine.com",
   # ]
   ```

## Après les changements

Redémarrez le serveur de développement Vite pour que les changements prennent effet :
```bash
npm run dev
```

