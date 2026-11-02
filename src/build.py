# Génère les gabarits e-mail (tableaux, styles en ligne, conditionnels Outlook, mode sombre).
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "emails"
OUT.mkdir(exist_ok=True)

INK, PAPER, LIME, MUTE, LINE = "#0f1a14", "#f6f4ee", "#c6f432", "#5f6b64", "#e3e0d6"
FONT = "'Helvetica Neue',Helvetica,Arial,sans-serif"
SERIF = "Georgia,'Times New Roman',serif"

def page(titre, preheader, corps):
    return f"""<!doctype html>
<html lang="fr" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no,address=no,email=no,date=no">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<title>{titre}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><style>td,th,div,p,a,h1,h2,h3{{font-family:Arial,sans-serif;mso-line-height-rule:exactly}}</style><![endif]-->
<style>
body{{margin:0;padding:0;width:100%!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}}
table{{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0}}
a{{text-decoration:none}}
@media only screen and (max-width:620px){{
  .w{{width:100%!important}} .px{{padding-left:22px!important;padding-right:22px!important}}
  .col{{display:block!important;width:100%!important;max-width:100%!important}} .col-pad{{padding:0 0 14px!important}}
  .h1{{font-size:34px!important;line-height:38px!important}} .big{{font-size:44px!important;line-height:46px!important}} .hide-m{{display:none!important}}
}}
@media (prefers-color-scheme:dark){{
  .bg{{background:#0b120e!important}} .card{{background:#131d17!important}} .tx{{color:#eef2ec!important}} .mu{{color:#9aa79f!important}} .bd{{border-color:#26332b!important}} .soft{{background:#1a261f!important}}
}}
[data-ogsc] .card{{background:#131d17!important}} [data-ogsc] .tx{{color:#eef2ec!important}} [data-ogsc] .mu{{color:#9aa79f!important}}
.force-dark .bg{{background:#0b120e!important}} .force-dark .card{{background:#131d17!important}} .force-dark .tx{{color:#eef2ec!important}} .force-dark .mu{{color:#9aa79f!important}} .force-dark .bd{{border-color:#26332b!important}} .force-dark .soft{{background:#1a261f!important}}
</style>
</head>
<body class="bg" style="margin:0;padding:0;background:{PAPER};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{PAPER};">{preheader}&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="bg" style="background:{PAPER};"><tr><td align="center" style="padding:28px 12px;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" class="w" style="width:600px;max-width:600px;">
{entete()}
{corps}
{pied()}
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr></table>
</body>
</html>
"""

def entete():
    return f"""<tr><td style="padding:0 4px 18px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td style="font-family:{FONT};font-size:22px;font-weight:700;letter-spacing:-1px;color:{INK};" class="tx"><span style="display:inline-block;width:22px;height:22px;background:{LIME};border-radius:11px;vertical-align:-4px;margin-right:6px;"></span>sika</td>
<td align="right" style="font-family:{FONT};font-size:12px;color:{MUTE};" class="mu"><a href="#" style="color:{MUTE};text-decoration:underline;" class="mu">Voir dans le navigateur</a></td>
</tr></table></td></tr>"""

def pied():
    return f"""<tr><td class="px" style="padding:26px 36px 10px;font-family:{FONT};font-size:12px;line-height:19px;color:{MUTE};" align="center">
<span class="mu" style="color:{MUTE};">Sika SA · Immeuble Harmony, boulevard de la Liberté, Akwa, Douala<br>Établissement de paiement agréé (exemple fictif). Sika ne vous demandera jamais votre code secret.<br><br>
<a href="#" style="color:{MUTE};text-decoration:underline;" class="mu">Préférences</a> &nbsp;·&nbsp; <a href="#" style="color:{MUTE};text-decoration:underline;" class="mu">Se désinscrire</a> &nbsp;·&nbsp; <a href="#" style="color:{MUTE};text-decoration:underline;" class="mu">Aide</a></span>
</td></tr>"""

def bouton(txt, bg=INK, fg="#ffffff", w=240):
    return f"""<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="#" style="height:50px;v-text-anchor:middle;width:{w}px;" arcsize="50%" stroke="f" fillcolor="{bg}"><w:anchorlock/><center style="color:{fg};font-family:Arial,sans-serif;font-size:16px;font-weight:bold;">{txt}</center></v:roundrect><![endif]--><!--[if !mso]><!--><a href="#" style="display:inline-block;background:{bg};color:{fg};font-family:{FONT};font-size:16px;font-weight:700;line-height:50px;padding:0 30px;border-radius:25px;mso-hide:all;">{txt}</a><!--<![endif]-->"""

def carte(contenu, pad="40px 36px", bg="#ffffff", extra=""):
    return f"""<tr><td class="card px" style="background:{bg};border-radius:22px;padding:{pad};{extra}">{contenu}</td></tr><tr><td style="height:12px;line-height:12px;font-size:12px;">&nbsp;</td></tr>"""

def T(txt, size=16, lh=25, color=INK, w=400, fam=FONT, cls="tx", extra=""):
    return f'<p class="{cls}" style="margin:0;font-family:{fam};font-size:{size}px;line-height:{lh}px;color:{color};font-weight:{w};{extra}">{txt}</p>'

# ——— 1. Newsletter mensuelle ———
def newsletter():
    hero = carte(f"""
{T('LE MOIS DE SIKA · NOVEMBRE 2026', 12, 18, MUTE, 700, cls='mu', extra='letter-spacing:2px;')}
<div style="height:14px;line-height:14px;font-size:14px;">&nbsp;</div>
<h1 class="h1 tx" style="margin:0;font-family:{SERIF};font-size:46px;line-height:50px;font-weight:400;color:{INK};letter-spacing:-1px;">Votre épargne a maintenant <span style="background:{LIME};color:{INK};padding:0 6px;">un objectif</span>.</h1>
<div style="height:18px;line-height:18px;font-size:18px;">&nbsp;</div>
{T('Rentrée, loyer, mariage, moto : créez une cagnotte, choisissez une date, et Sika met de côté un petit montant à chaque dépôt Mobile Money. Vous gardez la main à tout moment.', 17, 27, '#33413a')}
<div style="height:26px;line-height:26px;font-size:26px;">&nbsp;</div>
{bouton('Créer mon objectif')}
""", "44px 40px 40px")
    # bloc chiffre
    stat = carte(f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td class="col col-pad" width="50%" valign="top" style="padding-right:18px;">
<p class="big" style="margin:0;font-family:{SERIF};font-size:64px;line-height:64px;color:{LIME};letter-spacing:-2px;">1,2&nbsp;Md</p>
<p style="margin:8px 0 0;font-family:{FONT};font-size:14px;line-height:21px;color:#c9d3cc;">de francs CFA épargnés par la communauté Sika en octobre.</p></td>
<td class="col" width="50%" valign="top" style="border-left:1px solid #2a3a31;padding-left:22px;">
<p style="margin:0;font-family:{FONT};font-size:14px;line-height:22px;color:#c9d3cc;">L'objectif le plus populaire : <b style="color:#fff;">la rentrée scolaire</b>, avec 18 400 cagnottes ouvertes. Le plus original : un tracteur pour une coopérative de Foumbot.</p></td>
</tr></table>""", "34px 36px", INK)
    # trois nouveautés
    items = [("01", "Tontine numérique", "Invitez jusqu'à 30 membres, l'ordre de passage est tiré au sort et chacun voit les versements en direct."),
             ("02", "Retrait sans frais", "Le premier retrait du mois vers Orange Money ou MTN MoMo est désormais offert."),
             ("03", "Relevé en PDF", "Téléchargez un relevé signé, accepté pour vos dossiers de visa ou de location.")]
    rows = "".join(f"""<tr><td class="bd" style="border-top:1px solid {LINE};padding:20px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td width="56" valign="top" style="font-family:{SERIF};font-size:24px;color:{MUTE};" class="mu">{n}</td>
<td valign="top">{T(t, 18, 24, INK, 700)}<div style="height:4px;line-height:4px;font-size:4px;">&nbsp;</div>{T(d, 15, 23, MUTE, cls='mu')}</td></tr></table></td></tr>""" for n, t, d in items)
    nouv = carte(f"""{T('Les nouveautés du mois', 24, 30, INK, 400, SERIF)}<div style="height:16px;line-height:16px;font-size:16px;">&nbsp;</div><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>""")
    # deux colonnes
    deux = f"""<tr><td><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td class="col col-pad" width="50%" valign="top" style="padding-right:6px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="card" style="background:{LIME};border-radius:22px;padding:28px;">
{T('CONSEIL', 11, 16, INK, 700, extra='letter-spacing:2px;')}<div style="height:10px;line-height:10px;font-size:10px;">&nbsp;</div>{T('La règle des 3 enveloppes : besoins, envies, avenir. Sika la calcule pour vous.', 18, 25, INK, 700)}<div style="height:14px;line-height:14px;font-size:14px;">&nbsp;</div><a href="#" style="font-family:{FONT};font-size:14px;font-weight:700;color:{INK};text-decoration:underline;">Lire l'article</a>
</td></tr></table></td>
<td class="col" width="50%" valign="top" style="padding-left:6px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="card" style="background:#ffffff;border-radius:22px;padding:28px;">
{T('PARRAINAGE', 11, 16, MUTE, 700, cls='mu', extra='letter-spacing:2px;')}<div style="height:10px;line-height:10px;font-size:10px;">&nbsp;</div>{T('2 000 F pour vous, 2 000 F pour chaque proche qui ouvre un compte.', 18, 25, INK, 700)}<div style="height:14px;line-height:14px;font-size:14px;">&nbsp;</div><a href="#" style="font-family:{FONT};font-size:14px;font-weight:700;color:{INK};text-decoration:underline;" class="tx">Mon code : AMINA-27</a>
</td></tr></table></td>
</tr></table></td></tr><tr><td style="height:12px;line-height:12px;font-size:12px;">&nbsp;</td></tr>"""
    return page("Le mois de Sika — novembre 2026", "Nouveau : des objectifs d'épargne automatiques, et votre premier retrait du mois offert.", hero + stat + nouv + deux)

# ——— 2. Reçu de transaction ———
def recu():
    lignes = [("Bénéficiaire", "Mireille Ngo Bassong"), ("Numéro", "+237 6•• •• 41 07"), ("Opérateur", "MTN Mobile Money"), ("Motif", "Loyer novembre"), ("Date", "2 novembre 2026, 14 h 32"), ("Référence", "SK-7Q2M-48XD")]
    rows = "".join(f"""<tr><td class="bd mu" style="border-top:1px solid {LINE};padding:13px 0;font-family:{FONT};font-size:14px;color:{MUTE};">{a}</td><td class="bd tx" align="right" style="border-top:1px solid {LINE};padding:13px 0;font-family:{FONT};font-size:14px;color:{INK};font-weight:600;">{b}</td></tr>""" for a, b in lignes)
    corps = carte(f"""
<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td style="background:{LIME};border-radius:24px;width:48px;height:48px;text-align:center;font-family:{FONT};font-size:24px;font-weight:700;color:{INK};line-height:48px;">&#10003;</td></tr></table>
<div style="height:20px;line-height:20px;font-size:20px;">&nbsp;</div>
{T('Transfert envoyé', 15, 22, MUTE, 600, cls='mu')}
<p class="big tx" style="margin:6px 0 0;font-family:{SERIF};font-size:56px;line-height:58px;color:{INK};letter-spacing:-2px;">85&nbsp;000&nbsp;<span style="font-size:24px;letter-spacing:0;">FCFA</span></p>
<div style="height:8px;line-height:8px;font-size:8px;">&nbsp;</div>
{T('Frais : 0 F (premier transfert du mois offert)', 14, 21, MUTE, cls='mu')}
<div style="height:24px;line-height:24px;font-size:24px;">&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>
<div style="height:26px;line-height:26px;font-size:26px;">&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="soft" style="background:{PAPER};border-radius:14px;padding:16px 18px;">
{T('<b>Ce n\'est pas vous ?</b> Bloquez votre compte immédiatement en répondant STOP au 8 0 40, ou depuis l\'application, rubrique Sécurité.', 14, 21, '#33413a')}
</td></tr></table>
<div style="height:26px;line-height:26px;font-size:26px;">&nbsp;</div>
{bouton('Télécharger le reçu PDF', w=280)}
""", "40px 36px")
    return page("Reçu Sika — 85 000 FCFA envoyés", "Votre transfert de 85 000 FCFA à Mireille Ngo Bassong a bien été effectué.", corps)

# ——— 3. Invitation événement ———
def invitation():
    corps = carte(f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td style="font-family:{FONT};font-size:12px;font-weight:700;letter-spacing:2px;color:{LIME};">INVITATION · ENTRÉE LIBRE</td>
<td align="right" style="font-family:{FONT};font-size:12px;color:#9aa79f;">Places limitées</td></tr></table>
<div style="height:40px;line-height:40px;font-size:40px;">&nbsp;</div>
<h1 class="h1" style="margin:0;font-family:{SERIF};font-size:54px;line-height:56px;font-weight:400;color:#ffffff;letter-spacing:-2px;">Les Rencontres<br>de l'argent<br><i style="color:{LIME};">au féminin</i></h1>
<div style="height:28px;line-height:28px;font-size:28px;">&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td class="col col-pad" width="33%" valign="top" style="border-top:1px solid #2a3a31;padding-top:14px;"><p style="margin:0;font-family:{FONT};font-size:12px;color:#9aa79f;">Quand</p><p style="margin:4px 0 0;font-family:{FONT};font-size:16px;line-height:22px;color:#fff;font-weight:700;">Sam. 21 nov.<br>9 h – 13 h</p></td>
<td class="col col-pad" width="33%" valign="top" style="border-top:1px solid #2a3a31;padding-top:14px;"><p style="margin:0;font-family:{FONT};font-size:12px;color:#9aa79f;">Où</p><p style="margin:4px 0 0;font-family:{FONT};font-size:16px;line-height:22px;color:#fff;font-weight:700;">Institut français<br>Bonanjo, Douala</p></td>
<td class="col" width="33%" valign="top" style="border-top:1px solid #2a3a31;padding-top:14px;"><p style="margin:0;font-family:{FONT};font-size:12px;color:#9aa79f;">Avec</p><p style="margin:4px 0 0;font-family:{FONT};font-size:16px;line-height:22px;color:#fff;font-weight:700;">4 entrepreneures<br>et 1 notaire</p></td>
</tr></table>""", "40px 40px 44px", INK)
    prog = [("9 h 00", "Accueil, café et pagnes de la créatrice Ndomo"), ("9 h 45", "Table ronde : épargner avec un revenu irrégulier"), ("11 h 00", "Atelier : préparer un dossier de prêt qui passe"), ("12 h 15", "Questions au notaire : terrain, titre foncier, succession")]
    rows = "".join(f"""<tr><td class="bd mu" width="80" valign="top" style="border-top:1px solid {LINE};padding:14px 0;font-family:{FONT};font-size:14px;font-weight:700;color:{MUTE};">{h}</td><td class="bd tx" style="border-top:1px solid {LINE};padding:14px 0;font-family:{FONT};font-size:15px;line-height:22px;color:{INK};">{t}</td></tr>""" for h, t in prog)
    prog_c = carte(f"""{T('Au programme', 24, 30, INK, 400, SERIF)}<div style="height:12px;line-height:12px;font-size:12px;">&nbsp;</div><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>
<div style="height:28px;line-height:28px;font-size:28px;">&nbsp;</div>
<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td>{bouton('Je réserve ma place', LIME, INK, 250)}</td><td class="hide-m" style="padding-left:16px;font-family:{FONT};font-size:14px;"><a href="#" class="tx" style="color:{INK};text-decoration:underline;font-weight:600;">Ajouter à l'agenda</a></td></tr></table>""")
    return page("Invitation — Les Rencontres de l'argent au féminin", "Samedi 21 novembre à Douala : table ronde, atelier prêt et questions au notaire. Entrée libre.", corps + prog_c)

for nom, f in [("newsletter", newsletter), ("recu-transaction", recu), ("invitation", invitation)]:
    html = f()
    (OUT / f"{nom}.html").write_text(html, encoding="utf-8")
    print(nom, round(len(html.encode()) / 1024, 1), "Ko")
