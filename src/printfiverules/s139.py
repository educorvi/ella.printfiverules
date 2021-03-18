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

    template3page1path = (base_path / "resources/images/newtemplate3_seite1.jpg").resolve()
    pdf.image(str(template3page1path), x=-4, y=-8, w=217, h=313)

    data = {}
    input = input.get("data")

    # Kopffragen

    data["arbeitsstelle"] = input.get('#/properties/arbeitsstelle-arbeitsort')
    data["datum_uhrzeit"] = input.get('#/properties/datum-uhrzeit')
    data["person_anlageverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-anlagenverantwortlichen')
    data["person_arbeitsverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-arbeitsverantwortlichen')
    data["person_arbeitsausfuehrung"] = input.get('#/properties/arbeitsausfuhrende-person')

    if 'gegen elektrischen Schlag' in input.get('#/properties/zusatzliche-personliche-schutzausrustung-bei-der-1'):
        data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = "x"
    else:
        data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = ""

    if 'gegen Störlichtbogen' in input.get('#/properties/zusatzliche-personliche-schutzausrustung-bei-der-1'):
        data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = "x"
    else:
        data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = ""

    if input.get('#/properties/stehen-andere-anlagenteile-weiterhin-unter') == "ja":
        data["abgrenzung_arbeitsbereich_ja"] = "x"
    else:
        data["abgrenzung_arbeitsbereich_ja"] = ""

    if input.get('#/properties/stehen-andere-anlagenteile-weiterhin-unter') == "nein":
        data["abgrenzung_arbeitsbereich_nein"] = "x"
    else:
        data["abgrenzung_arbeitsbereich_nein"] = ""

    # 1A

    data["art_der_freischaltung1a"] = input.get('#/properties/edi8159e25519d24b4dbc510f0dab922d82')

    if data["art_der_freischaltung1a"] == "NH-Sicherungen":
        data["ausloesestrom1a"] = input.get('#/properties/edi6ccf2bd1724b46e18bba24ce7d36ff66')
    elif data["art_der_freischaltung1a"] == "NH-Lastschaltleiste":
        data["ausloesestrom1a"] = input.get('#/properties/ediac7a78d88db24a6aa920e61d3e887d16')
    elif data["art_der_freischaltung1a"] == "Leistungsschalter":
        data["ausloesestrom1a"] = input.get('#/properties/edic2673a81e3cf44b1a7500ff6d9b93952')
    else:
        data["ausloesestrom1a"] = "/"

    data["ort_der_freischaltung1a"] = input.get('#/properties/edi7ee749a5caa6420fa21d4882f14b2cb8')

    if data["ort_der_freischaltung1a"] == "Trafostation":
        data["nroderbezeichnung1a"] = input.get('#/properties/edid8d993f743324581b5c47c12b218efbb')
    elif data["ort_der_freischaltung1a"] == "Umspannwerk UW":
        data["nroderbezeichnung1a"] = input.get('#/properties/edi2b3d2eec597f488799007fdd7146012e')
    elif data["ort_der_freischaltung1a"] == "Kabelverteilerschrank":
        data["nroderbezeichnung1a"] = input.get('#/properties/edi2e295c0a64d742a4a3ef6e961e7d4efc')
    elif data["ort_der_freischaltung1a"] == "Maststation":
        data["nroderbezeichnung1a"] = input.get('#/properties/edi1e9e665dbf2a4118ba84a6910cfe9842')

    # 1B

    data["art_der_freischaltung1b"] = input.get('#/properties/edi0eb8d7909c5c439b9df0667d36440b38')

    if data["art_der_freischaltung1b"] == "NH-Sicherungen":
        data["ausloesestrom1b"] = input.get('#/properties/edif11bce386b3f45e19b95b1a80fd3ad17')
    elif data["art_der_freischaltung1b"] == "NH-Lastschaltleiste":
        data["ausloesestrom1b"] = input.get('#/properties/edi1163d69c077444199c8e513499a11ad9')
    elif data["art_der_freischaltung1b"] == "Leistungsschalter":
        data["ausloesestrom1b"] = input.get('#/properties/edi92e454031d0b47448f5a54bed57687c5')
    else:
        data["ausloesestrom1b"] = "/"

    data["ort_der_freischaltung1b"] = input.get('#/properties/edi2c1262bbdc134c72b2aa084d73af7fba')

    if data["ort_der_freischaltung1b"] == "Trafostation":
        data["nroderbezeichnung1b"] = input.get('#/properties/ediddcfbcaeae454ca592296dba6ea7933c')
    elif data["ort_der_freischaltung1b"] == "Umspannwerk UW":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi0e5df3f137304927b9fc8e6d49de9ddb')
    elif data["ort_der_freischaltung1b"] == "Kabelverteilerschrank":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi9e3a9cf861b649cd85df3cfe16e90081')
    elif data["ort_der_freischaltung1b"] == "Maststation":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi3de35e8419e74e8ba08256ee8309f962')

    # 2A

    data["schloss2a"] = input.get('#/properties/edid568fac032734a64ba0b76bec20256f9')
    data["schalten_verboten2a"] = input.get('#/properties/edifde90266c50b4decbbf39f90b1e78dc3')
    data["unbefugter_zugriff2a"] = input.get('#/properties/edib6a4d5aa3a2a49fda0289a286b0230d9')

    # 2B

    data["schloss2b"] = input.get('#/properties/edib2da15fb1b5b4be5946baaa5a817308b')
    data["schalten_verboten2b"] = input.get('#/properties/edieb2217b71929472192076587431dabea')
    data["unbefugter_zugriff2b"] = input.get('#/properties/edifde005a3ca474268861754c807311c2f')

    # 3A

    data["spannungspruefer3a"] = input.get('#/properties/edif1719b36a21943c9a074cf29c83f5b0f')

    # 3B

    data["spannungspruefer3b"] = input.get('#/properties/edi213b744312ab4abfb51b812aca8c901e')

    # 3C

    data["pruefungsart3c"] = input.get('#/properties/edi4e6f90e07b584199b2d6fddd01584650')

    # 4A

    data["stelle1"] = input.get('#/properties/edie262f477c18547b287fa143e61ae7dce')
    data["stelle2"] = input.get('#/properties/edib2c977060a8f4cea98a737707dc54d93')

    # Kopffragen

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(13, 107)
    pdf.set_text_color(0, 0, 0)
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

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_xy(20, 232)
    pdf.cell(0, 0, "ja")

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(14.4, 231.6)
    pdf.cell(0, 0, data.get("abgrenzung_arbeitsbereich_ja"))

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_xy(78, 232)
    pdf.cell(0, 0, "nein")

    pdf.set_font('DGUVMeta-Normal', '', 14)
    pdf.set_xy(72.2, 231.6)
    pdf.cell(0, 0, data.get("abgrenzung_arbeitsbereich_nein"))

    # Adding new page

    pdf.add_page()
    template7page2path = (base_path / "resources/images/newtemplate7_seite2.jpg").resolve()
    pdf.image(str(template7page2path), x=-4, y=-8, w=217, h=313)

    # 1a Freigeschaltet Ausschaltstelle 1

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 29.2)
    pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 34.2)
    pdf.cell(0, 0, data.get("art_der_freischaltung1a"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 40.7)
    pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 45.7)
    pdf.cell(0, 0, data.get("ort_der_freischaltung1a"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 52.2)
    pdf.cell(0, 0, 'Nr. oder Bezeichnung:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 57.2)
    pdf.cell(0, 0, data.get("nroderbezeichnung1a"))

    # 1b Freigeschaltet Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 89)
    pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 94)
    pdf.cell(0, 0, data.get("art_der_freischaltung1b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 100.5)
    pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 105.5)
    pdf.cell(0, 0, data.get("ort_der_freischaltung1b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 112)
    pdf.cell(0, 0, 'Nr. oder Bezeichnung:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 117)
    pdf.cell(0, 0, data.get("nroderbezeichnung1b"))

    # 2a Gegen Wiedereinschalten gesichert Ausschaltstelle 1

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 147.5)
    pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am Schalter eingehängt und abgeschlossen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 152.5)
    pdf.cell(0, 0, data.get("schloss2a"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 159)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 164)
    pdf.cell(0, 0, data.get("schalten_verboten2a"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 170.5)
    pdf.cell(0, 0, 'Wurden ausgebaute NH-Sicherungen unbefugtem Zugriff entzogen, z. B. mitgenommen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 175.5)
    pdf.cell(0, 0, data.get("unbefugter_zugriff2a"))

    # 2b Gegen Wiedereinschalten gesichert Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 196)
    pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am Schalter eingehängt und abgeschlossen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 201)
    pdf.cell(0, 0, data.get("schloss2b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 207.5)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 212.5)
    pdf.cell(0, 0, data.get("schalten_verboten2b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 219)
    pdf.cell(0, 0, 'Wurden ausgebaute NH-Sicherungen unbefugtem Zugriff entzogen, z. B. mitgenommen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 224)
    pdf.cell(0, 0, data.get("unbefugter_zugriff2b"))

    # 3a Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle1

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 256)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 261)
    pdf.cell(0, 0, data.get("spannungspruefer3a"))

    # Adding new page

    pdf.add_page()
    template8page3path = (base_path / "resources/images/newtemplate8_seite3.jpg").resolve()
    pdf.image(str(template8page3path), x=-4, y=-8, w=217, h=313)

    # 3b Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 22)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 27)
    pdf.cell(0, 0, data.get("spannungspruefer3b"))

    # 3c Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 50)
    pdf.cell(0, 0, 'Wie wurde geprüft?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 55)
    pdf.cell(0, 0, data.get("pruefungsart3c"))

    # 4a Geerdet und kurzgeschlossen an den Ausschaltstellen

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 79)
    pdf.cell(0, 0, 'an Ausschaltstelle 1:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 84)
    pdf.cell(0, 0, data.get("stelle1"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 90.5)
    pdf.cell(0, 0, 'an Ausschaltstelle 2:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 95.5)
    pdf.cell(0, 0, data.get("stelle2"))

    # 4b Geerdet und kurzgeschlossen an der Arbeitsstelle

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 105)
    pdf.cell(0, 0, 'Wurde eine ortsveränderliche EuK-Vorrichtung eingebaut?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 84)
    pdf.cell(0, 0, data.get("euk_unabhaengig"))

    pdf.output("s139.pdf", "F")

if __name__ == "__main__":
    from importdata import freileitungen as input
    create_pdf(input)