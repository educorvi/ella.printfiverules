from fpdf import FPDF
from pathlib import Path

def create_pdf(input):

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    base_path = Path(__file__).parent

    dguvnormalpath = (base_path / "resources/fonts/DGUVMeta-Normal.ttf").resolve()
    dguvboldpath = (base_path / "resources/fonts/DGUVMeta-Bold.ttf").resolve()
    dguvnormalitalicpath = (base_path / "resources/fonts/DGUVMeta-NormalItalic.ttf").resolve()

    pdf.add_font('DGUVMeta-Normal', '', dguvnormalpath, uni=True)
    pdf.add_font('DGUVMeta-Bold', '', dguvboldpath, uni=True)
    pdf.add_font('DGUVMeta-NormalItalic', '', dguvnormalitalicpath, uni=True)

    template2page1path = (base_path / "resources/images/newtemplate2_seite1.jpg").resolve()
    pdf.image(str(template2page1path), x=-4, y=-8, w=217, h=313)

    data = {}
    docid = input.get("docid")
    input = input.get("data")

    # Kopffragen

    data["arbeitsstelle"] = input.get('#/properties/arbeitsstelle-arbeitsort')
    jsontime = input.get('#/properties/datum-und-uhrzeit')
    try:
        if 'null' in jsontime:
            datetime = '%s.%s.%s' % (jsontime[8:10], jsontime[5:7], jsontime[:4])
        else:
            datetime = '%s.%s.%s %s' % (jsontime[8:10], jsontime[5:7], jsontime[:4], jsontime[11:])
    except:
        datetime = jsontime
    data["datum_uhrzeit"] = datetime

    data["person_anlageverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-anlagenverantwortlichen')
    data["person_arbeitsverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-arbeitsverantwortlichen')
    data["person_arbeitsausfuehrung"] = input.get('#/properties/arbeitsausfuhrende-person')

    data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = ""
    data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = ""
    if input.get('#/properties/zusatzliche-personliche-schutzausrustung-bei-der-1'):
        if 'gegen elektrischen Schlag' in input.get('#/properties/zusatzliche-personliche-schutzausrustung-bei-der-1'):
            data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = "x"

        if 'gegen Störlichtbogen' in input.get('#/properties/zusatzliche-personliche-schutzausrustung-bei-der-1'):
            data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = "x"

    # 1

    data["art_der_freischaltung"] = input.get('#/properties/edi4ed9533af063465dbd40ede7ce144b34')

    if data["art_der_freischaltung"] == "LS-Schalter":
        data["ausloesestrom"] = input.get('#/properties/edi595058c14f914f97913f1982c3ee63ed')
    elif data["art_der_freischaltung"] == "NH-Lastschaltleiste":
        data["ausloesestrom"] = input.get('#/properties/edi866e423a5ffe4c8d8c634335fa41d500')
    elif data["art_der_freischaltung"] == "Schraubsicherungen":
        data["ausloesestrom"] = input.get('#/properties/edidd592cc4a5674acfa8669da7e7056728')
    else:
        data["ausloesestrom"] = ""

    data["ort_der_freischaltung"] = input.get('#/properties/edi86c60abee95a45c8886de483c2b84e91')

    # 2

    data["sperrelement"] = input.get('#/properties/edi21ce1be420ec46bab9c030d670cd417f')
    data["schaltsperre"] = input.get('#/properties/edid27d8666a87a455c96e03b46bc81ed17')
    data["schalten_verboten"] = input.get('#/properties/edifef867c48d994dd7a9bead41c0a9dc1d')

    # 3

    data["spannungspruefer"] = input.get('#/properties/edi53fa934512eb411eaa2f82e45678d4bd')
    data["usv"] = input.get('#/properties/edi7c3c497dd89c4eaeb2c142b36a8a44b9')

    # 4

    data["euk_wo_eingebaut"] = input.get('#/properties/edib56dfa856ce84e9a92d61f2920c53f98')

    # 5

    data["ziel_der_abdeckung"] = input.get('#/properties/edi5cac8aded5f245d4964d289ba11c3d9d')

    if data["ziel_der_abdeckung"] == "ausreichender Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edi75d31cd8d2ac41e79bf6eb8ec77d6cca'))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edidff61f7941de460899c8868f6aa80c49'))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        entfernung_text = input.get('#/properties/edif0312b2bddd14667a88b0fd6f77f6efe')
        entfernung_meter = input.get('#/properties/edi9a40f15cc11b4fc7aafa2ce23b68e4d8')
        data["art_der_abdeckung"] = "%s %s m" % (entfernung_text, entfernung_meter)
    else:
        data["art_der_abdeckung"] = ""

    # Title

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 58.5)
    pdf.cell(0, 0, 'Arbeiten an')

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 68)
    pdf.cell(0, 0, 'Endstromkreisen')

    pdf.set_font('DGUVMeta-Bold', '', 14)
    pdf.set_text_color(0,140,142)
    pdf.set_xy(12.7, 83.5)
    pdf.cell(0, 0, 'Elektrohandwerk')

    # Kopffragen

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(13, 107)
    pdf.set_text_color(0,0,0)
    pdf.cell(0, 0, data.get("arbeitsstelle"))

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(13, 126)
    pdf.cell(0, 0, data.get("datum_uhrzeit"))

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(13, 145)
    pdf.cell(0, 0, data.get("person_anlageverantwortlichkeit"))

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(13, 164)
    pdf.cell(0, 0, data.get("person_arbeitsverantwortlichkeit"))

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(13, 183)
    pdf.cell(0, 0, data.get("person_arbeitsausfuehrung"))

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_xy(20, 208.5)
    pdf.cell(0, 0, "gegen elektrischen Schlag")

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(14.3, 208.3)
    pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_elektrischerschlag"))

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_xy(78, 208.5)
    pdf.cell(0, 0, "gegen Störlichbogen")

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(72.2, 208.3)
    pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_stoerlichtbogen"))

    #Adding new page

    pdf.add_page()
    template1page2path = (base_path / "resources/images/newtemplate1_seite2.jpg").resolve()
    pdf.image(str(template1page2path), x=-4, y=-8, w=217, h=313)

    # 1 Freigeschaltet

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 29.2)
    pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 34.2)
    pdf.cell(0, 0, data.get("art_der_freischaltung"))

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 39.2)
    pdf.cell(0, 0, 'Auslösestrom: %s A' % data.get("ausloesestrom"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 45.7)
    pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 50.7)
    pdf.cell(0, 0, data.get("ort_der_freischaltung"))

    # 2 Gegen Wiedereinschalten gesichert

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 77.5)
    pdf.cell(0, 0, 'Wurde ein Sperrelement eingesetzt, weil der Bereich für Laien zugänglich ist?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 82.5)
    pdf.cell(0, 0, data.get("sperrelement"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 89)
    pdf.cell(0, 0, 'Wurde eine Schaltsperre eingesetzt, weil der Bereich für Laien zugänglich ist?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 94)
    pdf.cell(0, 0, data.get("schaltsperre"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 100.5)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 105.5)
    pdf.cell(0, 0, data.get("schalten_verboten"))

    # 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 136)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 141)
    pdf.cell(0, 0, data.get("spannungspruefer"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 147.5)
    pdf.cell(0, 0, 'Dezentrale Einspeisung vorhanden, z. B. USV, PV, Notstromaggregat?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 152.5)
    pdf.cell(0, 0, data.get("usv"))

    # 4 Geerdet und kurzgeschlossen

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 189)
    pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung eingebaut?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 194)
    pdf.cell(0, 0, data.get("euk_wo_eingebaut"))

    # 5 Mit der Abdeckung soll erreicht werden

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 236.6)
    pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 241.6)
    pdf.cell(0, 0, data.get("ziel_der_abdeckung"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 248.1)
    if data["ziel_der_abdeckung"] != "Abdeckung nicht notwendig":
        pdf.cell(0, 0, 'Art der Abdeckung:')
    else:
        pdf.cell(0, 0, 'keine Abdeckung angebracht, weil: ')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 253.1)
    pdf.cell(0, 0, data.get("art_der_abdeckung"))

    return pdf.output('/tmp/%s.pdf' % docid, 'F')

if __name__ == "__main__":
    from importdata import endstromkreise as input
    create_pdf(input)
