import tkinter as tk
from tkinter import scrolledtext

# Create the main window
root = tk.Tk()
root.title("Genius Detector: Your Virtual Health Companion")

# Create and pack the input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Create and pack the symptom entry
symptom_label = tk.Label(input_frame, text="Enter your symptoms (comma-separated and in lowercase):")
symptom_label.pack(side=tk.LEFT)
symptom_entry = scrolledtext.ScrolledText(input_frame, width=40, height=5)
symptom_entry.pack(side=tk.LEFT, padx=10)

# Create the identify button
identify_button = tk.Button(root, text="Identify Virus")
identify_button.pack()

# Create and pack the result text widget
result_text = scrolledtext.ScrolledText(root, width=60, height=15)
result_text.pack(pady=10)

# Function to identify virus
def identify_virus():
    result_text.delete("1.0", tk.END)
    symptoms = symptom_entry.get("1.0", tk.END).lower().split(',')
    
    if not symptoms:
        result_text.insert(tk.END, "Please enter your symptoms.")
        return

    result_text.insert(tk.END, "============Identifying your Virus============\n\n")

    if 'fever' in symptoms or 'cough' in symptoms or 'runny nose' in symptoms:
        result_text.insert(tk.END, "You may have Flu\n\n")
        result_text.insert(tk.END, "Causes of the Flu:\nTransmission: Influenza viruses spread from person to person through respiratory droplets when an infected person coughs, sneezes, or talks. You can also get the flu by touching a surface or object that has the virus on it and then touching your mouth, nose, or eyes.\n\nTreatment of the Flu:\nAntiviral Medications, Rest\n\n")

    elif 'sneezing' in symptoms or 'sore throat' in symptoms or 'cough' in symptoms:
        result_text.insert(tk.END, "You may have Rhinovirus(common cold) \n\n")
        result_text.insert(tk.END, "Causes of Rhinovirus:\nTransmission: Rhinoviruses are highly contagious and spread through respiratory droplets when an infected person coughs or sneezes. They can also spread by touching contaminated surfaces and then touching the nose or mouth.\n\nTreatment of Rhinovirus:\n Stay Hydrated: Drinking plenty of fluids, such as water, herbal teas, and clear broths, helps keep the body hydrated and can help loosen mucus. \n\n")
    

    elif 'fever' in symptoms or 'difficulty breathing' in symptoms or 'sore throat' in symptoms:
        result_text.insert(tk.END, "You may have Parainfluenza virus \n\n")
        result_text.insert(tk.END, "Causes of Parainfluenza virus:\nTransmission: From someone nearby coughing or sneezing. Very small (microscopic) droplets containing HPIV can get into your nose or mouth directly through the air. They can also get on your hands, then get into your nose or mouth when you touch your face.\n\nTreatment Over-the-counter pain relievers such as acetaminophen (Tylenol) or ibuprofen (Advil, Motrin) can help reduce fever and alleviate discomfort. However, aspirin should not be given to children or teenagers with viral infections due to the risk of Reye's syndrome.\n\n")
   

    elif 'rash' in symptoms or 'sore throat' in symptoms or 'red eyes' in symptoms:
        result_text.insert(tk.END, "You may have Measles Virus \n\n")
        result_text.insert(tk.END, "Causes of the Measles:\nTransmission: Sharing drinks or food with someone with measles.\nShaking hands, holding hands or hugging someone with measles.\nTouching a surface containing the virus and then touching your mouth, nose or eyes.\n\nTreatment of Measles virus:\nThe most effective way to prevent measles is through vaccination. The measles, mumps, and rubella (MMR) vaccine is highly effective in preventing measles and is typically administered in two doses.\n\n")
        
   
    elif 'loss of taste' in symptoms or 'fever' in symptoms or 'difficulty breathing' in symptoms:
        result_text.insert(tk.END, "You may have Coronaviruses\n\n")
        result_text.insert(tk.END, "Causes of the Coronavirus:Virus Origin:\n COVID-19 is caused by the SARS-CoV-2 virus, which is a novel coronavirus that emerged in late 2019 in Wuhan, China.\nTransmission:\n The virus primarily spreads through respiratory droplets when an infected person coughs, sneezes, or talks. It can also spread by touching surfaces contaminated with the virus and then touching the face, especially the mouth, nose, or eyes.\n\nTreatment of the Corona virus:\nMild Cases:\n Most cases of COVID-19 are mild and can be managed at home. Treatment typically involves rest, staying hydrated, and taking over-the-counter medications to alleviate symptoms like fever and pain (e.g., acetaminophen).\nSevere Cases: In severe cases where individuals experience difficulty breathing, persistent chest pain, confusion, bluish lips or face, or other severe symptoms, medical attention should be sought immediately. Hospitalization may be necessary, and treatment might include supplemental oxygen, mechanical ventilation, and medications such as corticosteroids and antiviral drugs.\nVaccination: Vaccines against COVID-19 have been developed and are being administered globally to prevent infection and reduce the severity of the disease. Vaccination campaigns aim to achieve herd immunity and control the spread of the virus.\n\n")    

    elif 'muscle pain' in symptoms or ('joint pain' in symptoms or 'rash' in symptoms):
        result_text.insert(tk.END, "You may have Dengue Virus\n\n")
        result_text.insert(tk.END, "Causes of the Dengue Virus:\nTransmission: When a mosquito infected with the dengue virus bites a person, the virus enters the bloodstream, leading to infection.\n\nTreatment of the Dengue virus: \nFluid Replacement: Adequate fluid intake is crucial to prevent dehydration, especially in cases of severe dengue. Oral rehydration solutions or intravenous fluids may be administered to maintain hydration.\n\n")   


    elif 'muscle pain' in symptoms or ('headache' in symptoms or 'rash' in symptoms):
        result_text.insert(tk.END, "You may have Chikungunya Virus\n\n")
        result_text.insert(tk.END, "Causes of the Chikungunya Virus:\nTransmission: It is primarily transmitted to humans through the bite of infected Aedes mosquitoes, particularly Aedes aegypti and Aedes albopictus. These mosquitoes are daytime biters.\n\nTreatment of the Chikungunya virus: \n Using topical treatments or creams for rashes and taking antihistamines for itching can provide relief from skin-related symptoms.\n\n")   

        
    elif 'headache' in symptoms or ('cough' in symptoms or 'shortness of breath' in symptoms):
        result_text.insert(tk.END, "You may have Hantavirus\n\n")
        result_text.insert(tk.END, "Causes of the Hantavirus VirusHantavirus can affect anyone who comes in contact with infected mouse or rat poop, pee or spit. Cases occur throughout the world.\n\nTreatment of the Hantavirus: \n  in severe cases of hantavirus pulmonary syndrome (HPS), patients may require hospitalization and intensive care.\n Supportive measures may include oxygen therapy to help with breathing difficulties and intravenous fluids to maintain hydration.\n\n") 

    elif 'paralysis' in symptoms or ('muscle aches' in symptoms or 'coma' in symptoms):    
        result_text.insert(tk.END, "You may have West Nile Virus\n\n")
        result_text.insert(tk.END, "Causes of the West Nile Virus:\nTransmission: infected mosquitos transmit West Nile virus. They usually get the virus by biting an infected bird . The virus multiplies inside the mosquito, and it’s transmitted to you  when it bites you.\n\nTreatment of the West Nile virus: \n For individuals with mild symptoms, supportive care is often recommended, which may include rest, over-the-counter pain relievers to reduce fever and relieve symptoms, and staying hydrated. In more severe cases, where the virus causes neuroinvasive disease, such as encephalitis or meningitis, hospitalization and supportive therapy may be required.\n\n")   


    elif 'fatigue' in symptoms or ('fever' in symptoms or 'swollen lymph nodes' in symptoms):    
        result_text.insert(tk.END, "You may have Immunodeficiency Virus\n\n")
        result_text.insert(tk.END, "Causes of the Immunodeficiency Virus:\nTransmissioHIV is a virus that attacks the immune system, specifically targeting CD4 cells, which are a type of white blood cell that plays a crucial role in the body's defense against infection. HIV weakens the immune system over time, making it difficult for the body to fight off infections and diseases.\n\nTreatment of the Immunodeficiency virus:\nHIV is treated with a combination of medicines (pills) taken by mouth every day. This combination of pills is called antiretroviral therapy (ART).\n\n")


    elif 'nausea' in symptoms or 'vomiting' in symptoms or 'diarrhea' in symptoms:
        result_text.insert(tk.END, "You may have Rift Valley Fever\n\n")
        result_text.insert(tk.END, "Causes of the Rift Valley Fever:\nAnimal Contact: Humans can also get infected through direct contact with blood, body fluids, or tissues of infected animals, particularly during slaughtering, butchering, or handling infected animals.Consumption of Contaminated Products: Drinking unpasteurized milk from infected animals can also transmit the virus to humans.\n\nTreatment of the Rift Valley Fever:\n \n Symptomatic Treatment: Fever, pain, and other symptoms can be managed with antipyretics (fever-reducing medications) such as acetaminophen or ibuprofen.\n Rest and Hydration: Patients are advised to get plenty of rest and stay well-hydrated to help the body fight off the infection and maintain proper fluid balance\n\n")


    elif 'fever' in symptoms or 'headache' in symptoms or 'swollen salivary glors' in symptoms:
        result_text.insert(tk.END, "You may have Mumps virus\n\n")
        result_text.insert(tk.END, "Causes of the Mumps virus:\nTransmission: The mumps virus is spread through respiratory droplets, such as saliva, from an infected person. It can spread through:\nCoughing\nSneezing\n\nSharing utensils or cups with infected individuals.\n\nTreatment of the Mumps virus:\nVaccination: The best way to prevent mumps is through vaccination. The measles, mumps, and rubella (MMR) vaccine is highly effective in preventing mumps infection.\n\n")

        
    elif 'headache' in symptoms or ('confusion' in symptoms or 'seizures' in symptoms):    
        result_text.insert(tk.END, "You may have Herpes Simplex Virus (HSV)\n\n")
        result_text.insert(tk.END, "Causes of the Herpes Simplex Virus (HSV):\n HSV is highly contagious and is typically spread through direct contact with infected skin or mucous membranes.\n\nTreatment of the HSV:\n Antiviral Medications: Doctors often prescribe antiviral medications to manage HSV outbreaks. These medications, such as acyclovir, valacyclovir, and famciclovir, can help reduce the severity and duration of symptoms when taken during outbreaks.\n creams and ointments containing docosanol or lidocaine, can help relieve pain, itching, and discomfort associated with HSV sores.\n\n")


    elif 'anxiety' in symptoms or ('confusion' in symptoms or 'hydrophobia' in symptoms):    
        result_text.insert(tk.END, "You may have Rabies Virus\n\n")
        result_text.insert(tk.END, "Causes of the Rabies Virus:\n Rabies is caused by the rabies virus, which is primarily transmitted through the saliva of infected animals. The virus can enter the body through a bite or scratch from an infected animal, allowing the virus to spread to the central nervous system.\n\nTreatment of the Rabies virus: \nRabies Vaccine: The rabies vaccine is given in a series of shots over a specific time frame. The vaccine helps your body develop immunity to the rabies virus.\n Wound Care: Proper wound care, including washing the wound thoroughly with soap and water, can help reduce the risk of infection.\n\n")


    elif 'deafness' in symptoms or 'eye defects' in symptoms:
        result_text.insert(tk.END, "You may have  German Measles\n\n")
        result_text.insert(tk.END, "Causes of the  German Measles: German measles is caused by the rubella virus, which is transmitted through respiratory droplets when an infected person coughs or sneezes.It can also spread through direct contact with respiratory secretions or the rash of an infected person.\n\nTreatment of the German Measles: \nGerman measles often resolves on its own without specific medical treatment in healthy individuals.\n\n")


    elif 'neck stiffness' in symptoms or ('confusion' in symptoms or 'tremors' in symptoms):
        result_text.insert(tk.END, "You may have Encephalitis Virus\n\n")
        result_text.insert(tk.END, "Causes of the Encephalitis Virus: \nThe most common cause is when certain viruses affect your brain.That usually happens if you have the herpes simplex virus (HSV). But you can develop encephalitis if you have certain infectious diseases or other viruses.\n\nTreatment of the Encephalitis Virus:\nSupportive Care: Supportive care is essential to manage symptoms and provide comfort to the patient. This may include measures such as hydration, fever reduction, and pain management.\n Hospitalization: Severe cases of viral encephalitis may require hospitalization, especially if the patient experiences seizures, altered consciousness, or other neurological symptoms that need close monitoring and medical intervention.\n\n")


    elif 'redness in eyes' in symptoms or 'itching in eyes' in symptoms or 'pain in eyes' in symptoms:    
        result_text.insert(tk.END, "You may have Pink Eye Virus\n\n")
        result_text.insert(tk.END, "Causes of the Pink Eye Virus:\nBacterial infections can lead to pink eye.\n\nTreatment of the Pink Eye virus:\n Typically resolves on its own without specific treatment.\nHowever, the following measures may be helpful: \n Use cool compresses to soothe the eyes or reduce discomfort.\nPractice good hygiene, including frequent horwashing or avoiding touching or rubbing the eyes.\nAvoid sharing towels, pillowcases, or eye makeup with others to prevent spreading the virus.\n\n")


    elif 'pain in eyes' in symptoms or 'swelling in eyes' in symptoms or 'tears' in symptoms:
        result_text.insert(tk.END, "You may have Stye\n\n")
        result_text.insert(tk.END, "Causes of the Stye:\nInfection of an eyelash follicle.\n\nTreatment of the Stye:\n Warm compresses or sometimes antibiotics.\n\n")


    elif 'redness in eyes' in symptoms or 'blurred vision' in symptoms:    
        result_text.insert(tk.END, "You may have Uveitis\n\n")
        result_text.insert(tk.END, "Causes of the Uveitis:\nInflammation of the uvea (middle layer of the eye).\n\nTreatment of the Uveitis:\n Eye drops, antiviral medications, or surgery (in severe cases).\n\n")


    elif 'redness in eyes' in symptoms or 'swelling in eyes' in symptoms or 'pain in eyes' in symptoms:    
        result_text.insert(tk.END, "You may have Cellulitis\n\n")
        result_text.insert(tk.END, "Causes of the Cellulitis: \n Infection of the skin around the eye.\n\nTreatment of the Cellulitis: \n  Antibiotics, rest, or elevation of the affected area.\n\n")


    elif 'pain in eyes' in symptoms or 'discharge' in symptoms:
        result_text.insert(tk.END, "You may have Dacryocystitis\n\n")
        result_text.insert(tk.END, "Causes of the Dacryocystitis:\n Infection of the tear sac due to blocked tear ducts.\n\nTreatment of the Dacryocystitis:\n Warm compresses, antibiotics, or sometimes surgical intervention.\n\n")


    elif 'dry eyes' in symptoms or 'redness' in symptoms or 'itching in eyes' in symptoms:    
        result_text.insert(tk.END, "You may have Blepharitis\n\n")
        result_text.insert(tk.END, "Causes of the Blepharitis:\nBlepharitis is a common and chronic condition characterized by inflammation of the eyelids, particularly at the base of the eyelashes.\n\nTreatment of the Blepharitis:\n Medicated eyedrops and antibiotics.\n\n")


    elif 'itching on skin' in symptoms or 'redness on skin' in symptoms:    
        result_text.insert(tk.END, "You may have ECZEMA\n\n")
        result_text.insert(tk.END, "Causes of the ECZEMA:\nCombination of genetic, immune system, or environmental factors.\n\nTreatment of the ECZEMA:\n Moisturizing the skin regularly, avoiding triggers, using topical corticosteroids or other anti-inflammatory medications, or practicing good skincare habits.\n\n")


    elif 'formation of pimples' in symptoms or 'blackheads' in symptoms or 'cysts on the face':
        result_text.insert(tk.END, "You may have ACNE\n\n")
        result_text.insert(tk.END, "Causes of the ACNE:\nIncluding excess oil production, clogged hair follicles, bacteria (Propionibacterium acnes), hormonal changes, or inflammation.\n\nTreatment of the ACNE:\n Oral medications such as antibiotics, hormonal therapies (for women), or isotretinoin may be prescribed for severe cases.\n\n")

    elif 'persistent redness on skin' in symptoms or 'flushing' in symptoms or 'visible blood vessels':
        result_text.insert(tk.END, "You may have ROSACEA\n\n")
        result_text.insert(tk.END, "Causes of the ROSACEA:\nThe exact cause of rosacea is unknown, but it may involve genetic, environmental, vascular, or immune system factors.\n\nTreatment of the ROSACEA:\n Avoiding triggers such as sun exposure, alcohol, spicy foods, or stress. Topical medications (metronidazole, azelaic acid), oral antibiotics, or laser therapy may be prescribed to reduce redness or inflammation.\n\n")

    elif 'itching on skin' in symptoms or 'redness on skin' in symptoms or 'inflammation on skin':
        result_text.insert(tk.END, "You may have CONTACT DERMATITIS\n\n")
        result_text.insert(tk.END, "Causes of the CONTACT DERMATITIS:\n Contact dermatitis is caused by direct contact with substances that irritate the skin (e.g., detergents, chemicals) or trigger an allergic reaction (e.g., nickel, latex).\n\nTreatment of the CONTACT DERMATITIS:\n Avoiding triggers, applying topical corticosteroids or antihistamines to relieve symptoms, or using emollients or barrier creams to protect the skin.\n\n")

    elif 'thicknesson skin' in symptoms or 'redness on skin' in symptoms or 'scaly patches on skin':
        result_text.insert(tk.END, "You may have PSORIASIS\n\n")
        result_text.insert(tk.END, "Causes of the PSORIASIS:\n Psoriasis is an autoimmune disorder where the immune system mistakenly attacks healthy skin cells, leading to rapid turnover of skin cells or inflammation.\n\nTreatment of PSORIASIS:\n Topical corticosteroids, vitamin D analogs, retinoids, or moisturizers. In severe cases, phototherapy (light therapy), oral medications, or biologic drugs may be prescribed.\n\n")

    elif "genital warts" in symptoms or "abnormal vaginal bleeding" in symptoms or "bowel habits":
        result_text.insert(tk.END, "You may have Human papillomavirus\n\n")
        result_text.insert(tk.END, "Causes of the Human papillomavirus:\n transmitted thruogh skin-to-skin contact.\n\nTreatment of the Human papillomavirus:\n There is non cure for this virus but treatments are available for related symptoms.\n\n")

          
    elif "loss of apetite" in symptoms or "fatigue" in symptoms:
        result_text.insert(tk.END, "You may have Varicella-zoster virus\n\n")
        result_text.insert(tk.END, "Causes of the Varicella-zoster virus:\n It is transmitted direct contact with fluid from fromthe blisters of an infected person.\n\nTreatment of the Varicella-zoster virus:\n Antiviral medicines.\n\n")
        

    elif " muscle aches"in symptoms or "sore throat"in symptoms or " headache":    
        result_text.insert(tk.END, "You may have Coxsackievirus\n\n")
        result_text.insert(tk.END, "Causes of the Coxsackievirus:\nCoxsackievirus is caused by infection with the Coxsackievirus, a type of enterovirus belonging to the Picornaviridae family. It is transmitted through close contact with an infected person or by touching contaminated surfaces.\n\nTreatment of the Coxsackievirus:\n There is no specific cure for Coxsackievirus infections, so treatment focuses on relieving symptoms or providing supportive care.\n\n")


    elif "vomiting" in symptoms or "internal or external bleeding" in symptoms or "intense weakness":
        result_text.insert(tk.END, "You may have Ebola virus\n\n")
        result_text.insert(tk.END, "Causes of the Ebola virus:\nThe Ebola virus is believed to be animal borne,with bats bieng the most likely reservoir.\n\nTreatment of the Ebola virus:\n There is no specific cure for Ebola virus disease (EVD) approved by the FDA. However, supportive care such as maintaining electrolyte balance, providing oxygen therapy, or treating other infections can improve survival.\n\n")


    elif "nausea or vomiting"in symptoms or "abdominal pain" in symptoms or "facial swelling" in symptoms or "mucosal bleeding":
        result_text.insert(tk.END, "You may have Lassa virus\n\n")
        result_text.insert(tk.END, "Causes of the Lassa virus:\n Lassa virus is caused by infection with the Lassa virus, which is primarily transmitted to humans through contact with food or household items contaminated with rodent urine or feces.\n\nTreatment of the Lassa virus:\n Warm compresses or sometimes antibiotics.\n\n")



    elif "organ failure" in symptoms or "bleeding from nose,mouth or eyes" in symptoms or "jaundice" in symptoms or "red eyes,face or tounge":    
        result_text.insert(tk.END, "You may have yellow fever\n\n")
        result_text.insert(tk.END, "Causes of the yellow fever:\nIt is caused by the yellow fever virus,which is primarily transmitted to humans through bite of infected mosquitoes.\n\nTreatment of the yellow fever:\n By vaccination.\n\n")


    elif "sneezing" in symptoms or  "blood in the urine" in symptoms or "frequent urination" in symptoms or "rash":
        result_text.insert(tk.END, "You may have Adenovirus\n\n")
        result_text.insert(tk.END, "Causes of the Adenovirus:\n It is spread through close personal contact,respiratory droplets,or conatct eith conataminated surfaces.\n\nTreatment of the Adenovirus:\n There is no specific antiviral treatment so treatment focuses on managing symptoms.\n\n")


    elif "flu-like symptoms" in symptoms or "pneumonia" in symptoms or "hepatitis":
        result_text.insert(tk.END, "You may have Cytomegalovirus\n\n")
        result_text.insert(tk.END, "Causes of the Cytomegalovirus:\n It is caused by close-conatact with body fluids,such as salive,urinr,organ transplantation.\n\nTreatment of the Cytomegalovirus:\n Antiviral medicines can help manage symptoms or reduce the risk of complication especially in weakened immune system.\n\n")


    elif "blood in urine" in symptoms or "painful urination" in symptoms or "high blood pressure" in symptoms or "pain in the side or back":
        result_text.insert(tk.END, "You may have BK virus\n\n")
        result_text.insert(tk.END, "Causes of the BK virus:\nBK virus is a common virus that usually causes asymptomatic infection but can reactivate in people with weakened immune system.\n\nTreatment of the BK virus:\n There is no specific antiviral treatment but reducing immunosuppression in transplant reciepients or managing symptoms can help.\n\n")


    elif "infection" in symptoms or "itching sensation on skin" in symptoms or "burning during urination" in symptoms or "fever":
        result_text.insert(tk.END, "You may have Stye\n\n")
        result_text.insert(tk.END, "Causes of the Stye:\nInfection of an eyelash follicle.\n\nTreatment of the Stye:\n Warm compresses or sometimes antibiotics.\n\n")


    elif "anemia" in symptoms or "joint pain" in symptoms or "arthritis" in symptoms or "immune system disorders":
        result_text.insert(tk.END, "You may have Enterovirus\n\n")
        result_text.insert(tk.END, "Causes of the Enterovirus:\nSpread through close contact with infected person's respiratory secretion,feces,or conatminated surfces.\n\nTreatment of the Enterovirus:\n There is no specific antiviral treatment so treatment focuses on managing symptoms.\n\n")

    elif "high Fever" in symptoms or "rash" in symptoms or "Sswollen Glors:" in symptoms or "decreased appetite":
        result_text.insert(tk.END, "You may have Parvovirus B19\n\n")
        result_text.insert(tk.END, "Causes of the Parvovirus B19:\nIt is caused by close-conatact or from person to person.\n\nTreatment of the Parvovirus B19:\n Antiviral medicines can help manage symptoms or reduce the risk of complication especially in weakened immune system.\n\n")

    elif "Jaundice (yellowing of the skin or eyes)" in symptoms or "diarrhea" in symptoms or "Muscle aches" in symptoms or "fever":
        result_text.insert(tk.END, "You may have Cytomegalovirus\n\n")
        result_text.insert(tk.END, "Causes of the Cytomegalovirus:\nCytomegalovirus (CMV) is caused by infection with the cytomegalovirus, which is a member of the herpesvirus family.\n\nTreatment of the Cytomegalovirus:\n Antiviral medications can help manage symptoms and reduce complications, but there is no cure for cytomegalovirus (CMV) infection.\n\n")



# Bind the function to the button
identify_button.config(command=identify_virus)

# Start the GUI event loop
root.mainloop()

    

    
