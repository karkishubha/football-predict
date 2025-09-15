from django.db import models

class Player(models.Model):
    # Basic info
    player = models.CharField(max_length=255)
    market_value = models.CharField(max_length=100, null=True, blank=True)
    nation = models.CharField(max_length=100, null=True, blank=True)
    pos = models.CharField(max_length=50, null=True, blank=True)
    club = models.CharField(max_length=150, null=True, blank=True)
    league = models.CharField(max_length=150, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    # Playing stats
    mp = models.IntegerField("Matches Played", null=True, blank=True)
    starts = models.IntegerField(null=True, blank=True)
    minutes = models.IntegerField("Minutes Played", null=True, blank=True)
    goals = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    penalty = models.IntegerField("Penalties Scored", null=True, blank=True)
    pk_att = models.IntegerField("Penalty Attempts", null=True, blank=True)
    yellow_cards = models.IntegerField(null=True, blank=True)
    red_cards = models.IntegerField(null=True, blank=True)
    gls_per90 = models.FloatField("Goals per 90", null=True, blank=True)
    ast_per90 = models.FloatField("Assists per 90", null=True, blank=True)
    g_plus_a = models.FloatField("G+A", null=True, blank=True)
    gls_plus_ast = models.FloatField("Goals+Assists", null=True, blank=True)

    # Shooting stats
    sh = models.IntegerField("Shots", null=True, blank=True)
    sot = models.IntegerField("Shots on Target", null=True, blank=True)
    fk = models.IntegerField("Free Kicks", null=True, blank=True)
    sot_percent = models.FloatField("Shots on Target %", null=True, blank=True)
    sh_per90 = models.FloatField("Shots per 90", null=True, blank=True)
    sot_per90 = models.FloatField("Shots on Target per 90", null=True, blank=True)
    g_per_sh = models.FloatField("Goals per Shot", null=True, blank=True)
    g_per_sot = models.FloatField("Goals per Shot on Target", null=True, blank=True)

    # Defensive stats
    tackle = models.IntegerField(null=True, blank=True)
    tackle_won = models.IntegerField(null=True, blank=True)
    tackle_d = models.IntegerField("Tackles Defended", null=True, blank=True)
    tkl_percent = models.FloatField("Tackle %", null=True, blank=True)
    press = models.IntegerField(null=True, blank=True)
    succ_x = models.IntegerField(null=True, blank=True)
    succ_percent = models.FloatField("%", null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)
    shot_block = models.IntegerField("Shots Blocked", null=True, blank=True)
    interception = models.IntegerField("Interceptions", null=True, blank=True)
    clearance = models.IntegerField("Clearances", null=True, blank=True)

    # Passing stats
    passes_completed = models.IntegerField(null=True, blank=True)
    passes_attempted = models.IntegerField(null=True, blank=True)
    cmp_percent = models.FloatField("Completion %", null=True, blank=True)
    touches = models.IntegerField(null=True, blank=True)
    succ_y = models.IntegerField(null=True, blank=True)
    att = models.IntegerField(null=True, blank=True)
    
    # Misc
    number_of_players = models.IntegerField("#Pl", null=True, blank=True)

    def __str__(self):
        return f"{self.player} ({self.club})"
