import os
import pandas as pd
from django.core.management.base import BaseCommand
from players.models import Player

def safe_int(value):
    if pd.isna(value) or value == "":
        return None
    try:
        return int(value)
    except:
        return None

def safe_float(value):
    if pd.isna(value) or value == "":
        return None
    try:
        return float(value)
    except:
        return None

class Command(BaseCommand):
    help = "Import players from Final.xlsx into database"

    def handle(self, *args, **kwargs):
        file_path = os.path.join('predictor', 'Final.xlsx')  # adjust if needed
        df = pd.read_excel(file_path)

        # Drop unnamed/index columns
        df = df.drop(columns=[col for col in df.columns if "Unnamed" in col], errors="ignore")

        for _, row in df.iterrows():
            Player.objects.create(
                # Basic info
                player=row.get("Player"),
                market_value=row.get("Market value"),
                nation=row.get("Nation"),
                pos=row.get("Pos"),
                club=row.get("Club_x"),
                league=row.get("Leauge"),
                age=safe_int(row.get("Age")),

                # Playing stats
                mp=safe_int(row.get("MP")),
                starts=safe_int(row.get("Starts")),
                minutes=safe_int(row.get("Min")),
                goals=safe_int(row.get("Gls")),
                assists=safe_int(row.get("Ast")),
                penalty=safe_int(row.get("PK_x")),
                pk_att=safe_int(row.get("PKatt_x")),
                yellow_cards=safe_int(row.get("CrdY")),
                red_cards=safe_int(row.get("CrdR")),
                gls_per90=safe_float(row.get("Gls90")),
                ast_per90=safe_float(row.get("Ast90")),
                g_plus_a=safe_float(row.get("G+A")),
                gls_plus_ast=safe_float(row.get("Gls+Ast")),

                # Shooting stats
                sh=safe_int(row.get("Sh")),
                sot=safe_int(row.get("SoT")),
                fk=safe_int(row.get("FK")),
                sot_percent=safe_float(row.get("SoT%")),
                sh_per90=safe_float(row.get("Sh/90")),
                sot_per90=safe_float(row.get("SoT/90")),
                g_per_sh=safe_float(row.get("G/Sh")),
                g_per_sot=safe_float(row.get("G/SoT")),

                # Defensive stats
                tackle=safe_int(row.get("Tackle")),
                tackle_won=safe_int(row.get("TackleW")),
                tackle_d=safe_int(row.get("TakleD")),
                tkl_percent=safe_float(row.get("Tkl%")),
                press=safe_int(row.get("Press")),
                succ_x=safe_int(row.get("Succ_x")),
                succ_percent=safe_float(row.get("%")),
                blocks=safe_int(row.get("Blocks")),
                shot_block=safe_int(row.get("ShotB")),
                interception=safe_int(row.get("Int")),
                clearance=safe_int(row.get("Clr")),

                # Passing stats
                passes_completed=safe_int(row.get("Passes Completed")),
                passes_attempted=safe_int(row.get("Passes Attempted")),
                cmp_percent=safe_float(row.get("Cmp%")),
                touches=safe_int(row.get("Touches")),
                succ_y=safe_int(row.get("Succ_y")),
                att=safe_int(row.get("Att")),

                # Misc
                number_of_players=safe_int(row.get("#Pl")),
            )
        self.stdout.write(self.style.SUCCESS("Players imported successfully!"))
