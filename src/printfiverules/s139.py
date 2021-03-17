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

    data["zusaetzlichfreigeschaltet1a"] = input.get('#/properties/edi39026745e38e4279b3113e51c8d76d50')

    if data["zusaetzlichfreigeschaltet1a"] == [
        'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)']:
        data[
            "zusaetzlichfreigeschaltet1a"] = 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)'
    else:
        data["zusaetzlichfreigeschaltet1a"] = ''

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

    if data[
        "zusaetzlichfreigeschaltet1a"] == 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)':
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 63.7)
        pdf.cell(0, 0, 'Zusätzlich freigeschaltet:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 68.7)
        pdf.cell(0, 0, data.get("zusaetzlichfreigeschaltet1a"))
    else:
        data["zusaetzlichfreigeschaltet1a"] = ''

    pdf.output("s139.pdf", "F")

if __name__ == "__main__":
    from importdata import freileitungen as input
    create_pdf(input)