

def save_audit_data(sender, instance, **kwargs):
    if sender:
        instance.updatedBy = sender.username
    instance.save()
