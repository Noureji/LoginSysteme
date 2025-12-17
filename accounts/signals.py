from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import User

@receiver(post_migrate)
def create_default_groups_and_permissions(sender, **kwargs):
    """
    Crée les groupes Admin et User et assigne des permissions de base.
    """
    # 1️⃣ Créer les groupes
    admin_group, created = Group.objects.get_or_create(name='Admin')
    user_group, created = Group.objects.get_or_create(name='User')

    # 2️⃣ Créer les permissions
    content_type = ContentType.objects.get_for_model(User)

    # Permission pour gérer les utilisateurs
    can_manage_users, created = Permission.objects.get_or_create(
        codename='can_manage_users',
        name='Peut gérer les utilisateurs',
        content_type=content_type
    )

    # Permission pour voir le dashboard
    can_view_dashboard, created = Permission.objects.get_or_create(
        codename='can_view_dashboard',
        name='Peut voir le dashboard',
        content_type=content_type
    )

    # 3️⃣ Assigner les permissions aux groupes
    admin_group.permissions.add(can_manage_users, can_view_dashboard)
    user_group.permissions.add(can_view_dashboard)

    # Sauvegarder les groupes
    admin_group.save()
    user_group.save()

    print("Groupes et permissions par défaut créés avec succès.")
