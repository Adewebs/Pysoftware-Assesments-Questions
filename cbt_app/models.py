from django.db import models


class Question(models.Model):
    SEVERITY = [
        ("1", "Basic"),
        ("2", "Medium"),
        ("3", "High"),
        ("4", "Advanced"),
        ("5", "Highest")
    ]
    category = models.CharField(max_length=255, null=True, blank=True)  # Optional for now
    question_severity = models.CharField(max_length=1, choices=SEVERITY, null=True, blank=True)
    question_preamble = models.TextField(null=True, blank=True)
    question_main = models.TextField(null=True, blank=True)  # Main question
    a = models.CharField(max_length=255, blank=True, null=True)  # Option A
    b = models.CharField(max_length=255, blank=False)  # Option B
    c = models.CharField(max_length=255, blank=False)  # Option C
    d = models.CharField(max_length=255, blank=False)  # Option D
    e = models.CharField(max_length=255, blank=True, null=True)  # Option E (optional)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_main
