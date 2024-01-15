
import streamlit as st
import pandas as pd
import pickle
from pycaret.classification import *
# Function to load a model
# def load_model(model_name):
#     with open(model_name, 'rb') as file:
#         return pickle.load(file)

# Function to get user input for loan default prediction
def get_loan_default_input():

    region = st.selectbox("Select your region",['AFRICA', 'AFRICA EAST', 'AFRICA WEST', 'EAST ASIA AND PACIFIC',
       'EASTERN AND SOUTHERN AFRICA', 'EUROPE AND CENTRAL ASIA',
       'LATIN AMERICA AND CARIBBEAN', 'MIDDLE EAST AND NORTH AFRICA',
       'SOUTH ASIA', 'WESTERN AND CENTRAL AFRICA'])
    Country = st.selectbox("Select your country code",[ "Albania", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas, The", "Barbados", "Belarus", "Belgium", "Belize",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Bulgaria", "Cabo Verde",
    "Cameroon", "Chile", "China", "Colombia", "Congo, Democratic Republic of", "Costa Rica",
    "Cote d'Ivoire", "Croatia", "Cyprus", "Denmark", "Dominican Republic", "Eastern Africa",
    "Ecuador", "Egypt, Arab Republic of", "El Salvador", "Estonia", "Eswatini", "Ethiopia",
    "Fiji", "Finland", "Gabon", "Georgia", "Ghana", "Greece", "Grenada", "Guatemala",
    "Hungary", "Iceland", "India", "Indonesia", "Iran, Islamic Republic of", "Iraq", "Ireland",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Korea, Republic of", "Kosovo",
    "Latvia", "Lebanon", "Liberia", "Lithuania", "Luxembourg", "Macedonia, former Yugoslav Republic",
    "Macedonia, former Yugoslav Republic of", "Malawi", "Malaysia", "Mauritania", "Mauritius",
    "Mexico", "Moldova", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Netherlands",
    "New Zealand", "Nigeria", "North Macedonia", "Norway", "Pakistan", "Panama", "Papua New Guinea",
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Romania", "Russian Federation", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovak Republic", "Slovenia", "South Africa",
    "Southern Africa", "Spain", "Sri Lanka", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines",
    "Sudan", "Taiwan, China", "Tanzania", "Thailand", "Timor-Leste", "Tunisia", "Turkey", "Turkiye", "Uganda",
    "Ukraine", "Uruguay", "Uzbekistan", "Vietnam", "Yugoslavia, former", "Zambia", "Zimbabwe"
])
    
    Borrower = st.selectbox("Borrower",["ADDIS ABABA WATER AND SEWERAGE", "ADMIN DE LAS OBRAS SANITARIAS DEL ESTADO", "AGRICULTURAL DEVELOPMENT CORP.", "AGRICULTURAL DEVELOPMENT CORPO", "AGRICULTURE AND FISHERY DEVELOPMENT", "AMAPA SCR. DE PLANEJAMENTO ORCAMENTO", "AMEN BANK", "Ad Prenos Upra Elekenergtskiot SIS,Skopj", "Administración Nacional de Electricidad", "Azura Power West Africa Limited", "BAHIA COMPANIA DESENVOL  ACAO REGIO", "BAHIA SECRET. DESENVOL URBANO", "BAHIA SECRETARIA DE FAZENDA", "BANCA AGRICOLA, SA", "BANCA ROMANA PENTRU DEZVOLTARE", "BANCO DE MOCAMBIQUE", "BANKA CELJE D.D.", "BANOBRAS, SNC", "BORU HATLARI ILE PETROL TASIMA A.S.", "BULGARIAN DEPOSIT INSURANCE FUND", "BULGARIAN STATE RAILWAYS", "Banque de l'Habitat", "CAISSE AUTONOME D'AMORTISSEMENT", "CAISSE POUR LE FINANCEMENT ROUTIER", "CAIXA ECONOMICA FEDERAL - CAIXA", "CASSA PER IL MEZZOGIORNO", "CENTRAL AFRICAN POWER CORPORAT", "CHIEF EXECUTIVE", "CHIEF, DATA DIVISION", "CHINA DEV. CORP.", "COMMUNE URBAINE OF FES-MEDINA", "COMPANHIA METALURGICA NAC.", "CONTROLLER OF AID ACCOUNTS & AUDIT", "Consejo Provincial de Chimborazo", "Council of Ministers", "Croatian Bank for Reconstruction and Dev", "DEPARTAMENTO DE ANTIOQUIA", "DEPARTAMENTO DE LA GUAJIRA", "DIRECCAO GERAL DA TESOURO", "DIRECCION GENERAL DE", "DIRECCION GENERAL DE CULTURA Y EDUCACION", "DIRECCION GENERAL DE POLITICA", "DIRECTION OF FINANCE FINANCE DEPT.", "DISTRICT HEATING ENTERPRISE, KATOWICE", "Dedicated Freight Corridor Corporation", "Department of Finance", "Development Bank of The Philippines", "Direction G?ral de la Dette", "Direction General de la Dette", "Direction Generale de la Dette", "Director General, Budget Department", "ELECTRIC POWER DEVELOPMENT COM", "ELECTRICIDADE DE PORTUGAL", "ELECTRICITY AUTHORITY OF CYPRU", "ELECTRICITY GENERATING AUTH. OF THAILAND", "ELECTRICITY SUPPLY BOARD", "ELECTROCENTRALE DEVA S.A", "ELETROBRAS", "ENERGOGAS - RADNA ORG", "ESKOM HOLDINGS LIMITED", "ETHIOPIAN", "ETHIOPIAN TELECOMMUNICATION", "ETHIOPIAN TRANSPORT CONSTRUCT.", "Empresa Municipal  Agua Potable - EMAPAG", "FIJI ELECTRICITY AUTHORITY", "Federal Ministry of Finance", "Fin Nacional de Desarrollo Agropecuario", "Financiera de Desarrollo Nacional", "GENERAL ACCOUNTING OFFICE", "GENERAL MANAGER", "GREATER AMMAN MUNICIPALITY", "Governo do Distrito Federal", "H. M. TREASURY", "HANSHIN EXPRESSWAY PUBLIC CORP", "Head of Office, Minister's Staff Office", "ICETEX", "ILLER BANKASI", "IND. DEV. FIN. BERHAD", "IND. DEVELOPMENT BANK LIMITED", "INDUST. BANK OF KOREA", "INDUSTRIAL FINANCE CORPORATION", "INST. FIN. DE APOIO", "INV. & DEV. BK. OF MALAWI LTD.", "IPRAS MUDURIYET BINASI TUTUNCI", "ISTANBUL METROPOLITAN MUNICIPALITY", "India Infrastructure Finance Company Ltd", "JAPAN DEVELOPMENT BANK", "JSC Azerenerji", "KENYA PIPELINE COMPANY LIMITED", "KENYA RAILWAYS CORPN", "KOREA DEVELOPMENT BANK", "KOREA ELECTRIC POWER CORP.", "KOREA LONG TERM CREDIT BANK", "KOREA WATER RESOURCES CORP.", "KZ-Electricity Grid Operating comp-KEGOC", "LANDSVIRKJUN", "LIBERIAN BANK FOR INDUSTRIAL D", "Land Bank of The Philippines", "M.R. Transport J.S.C - Skopje", "MATO GROS SEC. DE ESTADO DE PLANEJAMENTO", "METROPOLITAN WATERWORKS AUTHORITY", "MIN. OF THE ENVIRONMENT", "MINISTER OF FINANCE", "MINISTER OF FINANCE & ECONOMIC AFFAIRS", "MINISTERE AFFAIRES ECON. ET DEVELOPMT", "MINISTERE DE L'ECONOMIE ET DES FINANCES", "MINISTERE DES FINANCES", "MINISTERIO DAS FINANCAS", "MINISTERIO DE ECONOMIA Y FINANZAS PUBLIC", "MINISTERIO DE FINANCAS E PLANO", "MINISTERIO DE HACIENDA", "MINISTERIO DE HACIENDA Y CREDITO PUBLICO", "MINISTERIO DE PLANIFICACION Y", "MINISTRE DES FINANCES",
                                        "MINISTRO DE ECONOMIA Y", "MINISTRY FINANCE AND CUSTOMS", "MINISTRY FOR FINANCE", "MINISTRY OF  FINANCE", "MINISTRY OF DEVELOPMENT PLANNING", "MINISTRY OF ECONOMIC AFFAIRS", "MINISTRY OF ECONOMIC AFFAIRS & FINANCE", "MINISTRY OF FIN & ECO DEVELOPMENT", "MINISTRY OF FIN & ECO EMPOWERMENT", "MINISTRY OF FINANCE", "MINISTRY OF FINANCE & ECO DEVELOPMENT", "MINISTRY OF FINANCE - Georgia", "MINISTRY OF FINANCE AND DEV. PLANNING", "MINISTRY OF FINANCE AND ECONOMIC AFFAIRS", "MINISTRY OF FINANCE, TRADE, INVESTMENT", "MINISTRY OF PLANNING", "MINISTRY OF PLANNING & INTNL COOPERATION", "MINISTRY OF PUBLIC  FINANCE", "MINISTRY OF THE ENVIRONMENT", "MINISTRY OF TREASURY AND FINANCE", "MORTGAGE BANK OF FINLAND OY", "MUNICIPAL HEATING ENTERPRISE IN KRAKOW", "MUNICIPALIDAD METROPOLITANA DE LIMA", "MUNICIPALITY DE TERESINA", "MUNICIPALITY OF BOGOTA", "MUNICIPALITY OF RECIFE", "MUNICIPALITY OF URUGUAIANA", "Mato Grosso Gabinete do Governador", "Metropolitan Waterworks And Sewerage", "Min de l'Economie et de la Prospective", "Min of Eco, Fin. and Invest. Support", "Minist? de l'Economie, de l'Emploi", "Ministere de l'Economie, de l'Emploi", "Ministere du Plan Et du Dev. Regional", "Ministerio De Economia Y Finanzas", "Ministerio de Economia y Finanzas", "Ministerio de Economia, Planificacion y", "Ministerio de Economía y Finanzas", "Ministerio de Finanzas Públicas", "Ministerio de Hacienda", "Ministry of Eco, Planning and RegionDev", "Ministry of Economic Affairs and Dev.", "Ministry of Economy", "Ministry of Finance", "Ministry of Finance & National Planning", "Ministry of Finance & Treasury", "Ministry of Finance & the Public Service", "Ministry of Finance - Macedonia", "Ministry of Finance - North Macedonia", "Ministry of Finance Labor and Transfers", "Ministry of Finance and Economy", "Ministry of Finance,", "Ministry of Finance, Dev. and Planning", "Ministry of Finance, Planning & Eco. Dev", "Ministry of International Cooperation", "Ministry of Planning and Finance", "Ministry of Treasury", "Ministry of Treasury and Finance", "Ministère de l Economie et de la Relance", "Ministère de l'Economie, de l'Emploi", "Ministère de l’Economie et de la Relance", "Ministério da Fazenda", "Municipality of Bage", "Municipality of Belo Horizonte", "Municipality of Manta", "Municipality of Rio Grande", "Municipality of Santa Maria", "Municipality of Santos", "Municipality of São Bernardo do Campo", "Município do Rio de Janeiro", "NATIONAL ELECTRICITY BOARD", "NATIONAL INVESTMENT BANK FOR", "NATIONAL TREASURY MANAGEMENT AGENCY", "NATIONAL TREASURY, ASSET & LIABILITY MGT", "NIGERIAN IND. DEV. BANK LTD.", "NIGERIAN NATIONAL PETROLEUM CORPORATION", "NIGERIAN PORTS AUTHORITY", "NIHON DORO KODAN", "NOVA LJUBLJANSKA BANKA", "National Electrification Administration", "National Power Corporation", "OESTERREICHISCHE ELEK A. G.", "OESTERREICHISCHE ELEKTRIZITAET", "OFFICE NATIONAL DE L'ASSAINISSEMENT", "ONEE of Morocco", "PARA - GABINETE DO GOVERNADOR", "PARAIBA SECRETARIA DE ESTADO DE PLANEJ", "PE MR Infrastructure - Skopje", "PEC GEOTERMIA PODHALANSKA, S. A.", "PETROLEUM AUTHORITY OF THAILAND", "PHILIPPINE NATIONAL BANK", "PORT AUTONOME DE DAKAR", "POWER GRID CORPORATION OF INDIA LIMITED", "POWER HOLDING CORPORATION OF NIGERIA PLC", "PREFEITURA MUNICIPAL DE BETIM (MG)", "PREFEITURA MUNICIPAL DE PELOTAS", "PREFEITURA MUNICIPAL DE SAO LUIS", "PREFEITURA MUNICIPAL DE UBERABA", "PRENA SECRETARIA DA FAZENDA", "PROVINCIA DE CORDOBA", "PROVINCIAL ELECTRICITY AUTHORITY", "PROVINCIAL WATERWORKS AUTHORITY", "PT Perusahaan Listrik Negara", "Pernanbuco Secretari de Estado de Planej",
                                        "Port of Ploce Authority", "Port of Rijeka Authority", "Prefeitura de Manaus", "Province of La Rioja", "Province of San Juan", "Provincia Buenos Aires", "Public Enterprise for State Roads", "QUIMIGAL-QUIMICA DE PORTUGAL", "REGIE NATIONALE DES CHEMINS DE", "REPUBLIC OF FINLAND", "REPUBLIC OF ICELAND", "REPUBLICKI FOND VODA", "RIGAS SILTUMS", "Republic of South Africa", "SABAH PORTS AUTHORITY", "SABESP", "SATLUJ JAL VIDYUT NIGAM LIMITED", "SECRETARIA DE DESENVOLVIMENTO RURAL", "SECRETARIA DE ESTADO DA FAZENDA", "SECRETARIA DE ESTADO DE TRANSPORTES", "SECRETARIA DE PLANEJAMENTO-RIO DE JANEIR", "SECRETARIA DO PLANEJAMENTO-PIAUI", "SECRETARIA GENERAL TECNICA", "SECRETARY TO THE GOVERNMENT OF", "SECRETARY TO THE TREASURY", "SIERRA LEONE ELECTRICITY CORP.", "SINAI YATIRIM VE KREDI BANKASI", "SKB BANKA D.D.", "SMALL INDUSTRIES DEVELOPMENT BK OF INDIA", "SOC. FUND FOR ROADS,SERBIA", "SOCAPALM", "SOCIEDADES REUNIDAS FABRICA", "SOCIETE NATIONALE D'EXPLOITATION", "SR. DIRECTOR GENERAL DE LA RED", "STATE EXPORT-IMPORT BANK OF UKRAINE", "STATE OF ALAGOAS", "STOPANSKA BANKA", "Secretaria De Hacienda Y Credito Publico", "Secretaria de Hacienda Y Credito Publico", "Sociedad Hipotecaria Federal S.N.C", "Southern Gas Corridor CJSC", "State of Acre", "State of Amazonas", "State of Ceará", "State of Espírito Santo", "State of Minas Gerais", "State of Parana", "State of Rio Grande Do Sul", "State of Rio Grande do Norte", "State of Rio de Janeiro", "State of Santa Catarina", "State of Sergipe", "Subic Bay Metropolitan Authority", "São Paulo Secretaria do Estado", "T. C. ZIRAAT BANKASI", "T. Vkiflar Bankasi T.A.O", "TAIWAN POWER COMPANY", "TANGANYIKA DEV. FIN. CO. LTD.", "TELECOM AUTHORITY OF SINGAPORE", "TELEPHONE ORGANIZATION OF THAILAND", "TEOLLISTAMISRAHASTO OY -", "TERMOELECTRICA S.A", "THE BOTSWANA DEVELOPMENT CORPO", "THE DEVELOPMENT BANK OF SINGAP", "THE INDUSTRIAL CREDIT COMPANY,", "THE MALAYAN RAILWAY ADMINISTRA", "THE SECRETARY", "THE STATE RAILWAYS OF THAILAND", "TOKYO EXPRESSWAY PUBLIC CORPOR", "TRANSELECTRICA S.A", "TURKIYE ELEKTRIK DAGITIM A.S. (TEDAS)", "TURKIYE HALK BANKASI A.S", "TURKIYE IHRACAT KREDI BANKASI A.S.", "TURKIYE KALKINMA BANKASI A. S.", "TURKIYE KALKINMA VE YATIRIM BANKASI", "TURKIYE SINAI KALKINMA BANKASI A.S.", "The National Treasury and Planning", "Tocantins Secretaria do Planejamento", "UNDERSECRETARIAT OF TREASURY", "VILNIUS DISTRICT HEATING CO", "VOJVODJANSKA - UDRUZENA BANKA", "VORARLBERGER ILLWERKE AKTIENGE", "WORLD BANK OFFICE", "YUGOSLAV INVESTMENT BANK", "ZAJEDNICA JUGOSLOVENSKIH ZELEZ", "ZARZAD MORSKIEGO PORTU SZCZECIN-SWINOUJS", "Zimbabwe Electricity Supply Commission"])
    
    Gaurantor = st.selectbox("Gaurantor", ["Albania", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Azerbaijan", "Bahamas, The", "Barbados", "Belarus", "Belgium", "Belize", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Bulgaria", "Cabo Verde", "Cameroon", "Caribbean", "Chile", "China", "Colombia", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cyprus", "Dominican Republic", "Ecuador", "Egypt, Arab Republic of", "El Salvador", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Gabon", "Georgia", "Ghana", "Grenada", "Guatemala", "Hungary", "India", "Indonesia", "Iran, Islamic Republic of", "Iraq", "Jamaica", "Jordan", "Kazakhstan", "Kenya", "Korea, Republic of", "Kosovo", "Latvia", "Lebanon", "Liberia", "Lithuania", "Macedonia, former Yugoslav Republic", "Macedonia, former Yugoslav Republic of", "Malawi", "Malaysia", "Mauritania", "Mauritius", "Mexico", "Moldova", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Nigeria", "North Macedonia", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Romania", "Russian Federation", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Slovak Republic", "Slovenia", "South Africa", "Sri Lanka", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines", "Sudan", "Taiwan, China", "Tanzania", "Thailand", "Timor-Leste", "Tunisia", "Turkey", "Turkiye", "Uganda", "Ukraine", "United Kingdom", "Uruguay", "Uzbekistan", "Vietnam", "Zambia", "Zimbabwe"]
)
    LoanTy = st.selectbox("Loan Type", ['BLOAN', 'CPL', 'FSL', 'GUBF', 'GURB', 'NON POOL', 'POOL LOAN', 'SCL',
       'SCP EUR', 'SCP USD', 'SCPD', 'SCPM', 'SNGL CRNCY'])

    interestR = st.number_input("InterestRate", min_value=0.0, max_value=100.0)
    # ...

    PrincipalA = st.number_input("Original Principal Amount", min_value=0.0, max_value=1000000000000.0)

    return pd.DataFrame([[region, Country, Borrower, Gaurantor, LoanTy, interestR, PrincipalA]],
                         columns=['Region', 'Country', 'Borrower', 'Guarantor', 'Loan Type', 'Interest Rate', 'Original Principal Amount'])
 
# ...

def main():
    st.sidebar.title("Select Task")
    task = st.sidebar.selectbox("Choose a task",
                                ["Loan Disbursement Prediction",
                                 "Claim Prediction",
                                 "Spam Filtering"])

    st.title("Machine Learning Catalogue Models")

    if task == "Loan Disbursement Prediction":
        user_input = get_loan_default_input()
        #setup()

        model = load_model('loan_default_model')
        if st.button('Predict'):
            prediction = predict_model(model, user_input)
            prediction = prediction["prediction_label"][0]
            if prediction == 0:
                st.write("The loan is likely to be cancelled")
            else:
                st.write("The loan is likely to be approved and fully disbursed")


    elif task == "Spam Filtering":
            # Textbox for user input
        user_input = st.text_area("Enter text:")
        user_input = [user_input]
        with open('spam_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
    
    # Check for Spam button
        if st.button("Check for Spam"):
            predict1 =  model.predict(user_input)
            if predict1 == 1:
                st.warning("This text might be spam!")
            else:
                st.success("This text is not spam.")
       # 
          #      

   # elif task == "Claim Prediction":
     #   user_input = get_claim_prediction_input()
       # model = model = load_model('claim_prediction_model.pkl')

    # if st.button('Predict'):
    #     prediction = model.predict(user_input)
    #     st.write(f"Prediction: {prediction[0]}")

if __name__ == '__main__':
    main()
