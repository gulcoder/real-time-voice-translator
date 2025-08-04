# Realtidsöversättare med känsloanalys (→ Engelska)

En avancerad Python-applikation som spelar in, transkriberar och översätter tal i realtid, samtidigt som den analyserar och anpassar den emotionella tonen i både text och röst. Lösningen kombinerar flera AI-tekniker för att skapa en naturlig, kontext- och känsloanpassad översättning med röståtergivning.

---

## Översikt

Detta projekt syftar till att möjliggöra smidig kommunikation mellan språk och kulturer, med en extra dimension av känsloigenkänning som förbättrar användarupplevelsen. Genom att analysera både talets innehåll och den emotionella prosodin i rösten kan systemet anpassa ton, hastighet och betoning i den genererade rösten – vilket skapar en mer engagerande och autentisk konversation.

---

## Teknisk Arkitektur & Teknikstack

- **Talupptagning:** Inspelning via `sounddevice` med WAV-format och 16 kHz sampling, för optimal ljudkvalitet och kompatibilitet.
- **Tal-till-text:** OpenAI Whisper används för kraftfull och exakt transkribering, stöd för svenska med hög precision.
- **Emotionell Analys:**
  - **Textbaserad:** Enkel ordbaserad känsloidentifiering för att fånga känslomässiga signaler i innehållet.
  - **Röstbaserad:** Librosa används för att extrahera pitch och energifunktioner, som används för basal känsloanalys.
- **Översättning och tonanpassning:** GPT-4 eller liknande LLM för kontextmedveten och känsloanpassad översättning, möjliggör både formell och informell ton.
- **Röstsyntes:** Text-till-tal med tonjustering (tempo, pitch, volym) baserat på emotionell analys, för naturlig återgivning.

---

## Funktioner & Möjligheter

- **Real-tidsbearbetning:** Snabb inspelning, transkribering, analys och röstgenerering.
- **Flerskiktad känsloanalys:** Kombinerar text- och röstdata för bättre tolkning av användarens känslor.
- **Ton- och stilanpassning:** Styr röstsyntesen att matcha känslor som neutral, glad, arg osv.
- **Flerspråkighet:** Bygger på skalbar arkitektur med stöd för flera käll- och målspråk.
- **Modulärt och utbyggbart:** Varje del (inspelning, transkribering, emotion, översättning, syntes) kan ersättas eller förbättras oberoende.

---

## Användningsområden

- **Internationella kundtjänster:** Förbättra kundupplevelsen med känsloanpassade översättningar i realtid.
- **Distansmöten och konferenser:** Automatisera översättning med tonanpassning för att minska missförstånd.
- **Tillgänglighet:** Hjälp för personer med språk- eller talhandikapp, som behöver emotionellt nyanserad översättning.
- **Språkinlärning:** Ge elever feedback inte bara på vad som sägs utan hur det sägs.
- **Forskning och utveckling:** Bas för att testa och utveckla avancerade modeller för tal- och känsloanalys.

---

## Framtida Utvecklingsmöjligheter

- Integration av transformer-baserade emotiondetektorer (t.ex. Hugging Face Speech Emotion Recognition)
- Djupare prosodi- och kontextanalys för ännu mer nyanserad röstsyntes
- Stöd för längre konversationer och dialoghantering
- Web- och mobilgränssnitt för bredare användning
- Optimering för edge-enheter och realtidsrespons utan kraftig serverinfrastruktur

---

## Teknisk Fördjupning

- **Librosa:** Ljudanalys och extraktion av prosodiska features som pitch och energi.
- **OpenAI Whisper:** Multispråkig taligenkänning baserad på transformerarkitektur.
- **OpenAI GPT-4:** Kraftfull textgenerering och översättning med känslomässig tonanpassning.
- **Text-till-tal:** Anpassad röstsyntes som manipulerar hastighet, volym och pitch baserat på emotionell input.
- **Python 3.12:** Senaste version med kompatibilitet för AI- och ljudbibliotek.

---

## Licens & Bidrag

Detta projekt är licensierat under MIT-licensen. Bidrag är välkomna genom pull requests eller issue-rapportering på GitHub.

---

## Kontakt

För frågor, förslag eller samarbete, kontakta mig via GitHub.
