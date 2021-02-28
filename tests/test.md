Copyright ©Giorgi Saatashvili. All rights reserved

# 7. **D FLIP FLOP**
იმისათვის რომ კარგად შეძლოთ ამ თავში არსებული მასალის გააზრება აუცილებელია
გესმოდეთ [SR ტრიგერის](https://en.wikipedia.org/wiki/Flip-flop_(electronics)#Simple_set-reset_latches) მუშაობის პრინციპი, ამიტომ თუ თვლით რომ გაქვთ ლაფსუსები
გთხოვთ, გადახედოთ თავს ზემოაღნიშნულ ტრიგერზე.


## 7.1 **ისტორია**

როგორც უკვე კარგად ვიცით [SR ტრიგერს](https://en.wikipedia.org/wiki/Flip-flop_(electronics)#Simple_set-reset_latches) აქვს [აკრძალული მდგომარეობა](https://en.wikipedia.org/wiki/Flip-flop_(electronics)#Simple_set-reset_latches), რაშიც
იგულისხმება რომ შესასვლელების გარკვეული კომბინაციისას ვერ დავადგენთ
გამომავალ სიგნალს. ჩვენ შეგვიძლია SR ტრიგერი გადავაკეთოთ ისე რომ
აღარ არსებობდეს მისთვის აკრძალული მდგომარეობა. თუ გავიხსენებთ SR ტრიგერს,
გამომდინარე იქედან, თუ რომელი ლოგიკური ელემენტებით აიგება (NAND თუ NOR)
აკრძალული მდგომარეობა ექმნება S,R-ის განსხვავებულ მნიშვნელობებზე (0,0 და 11
შესაბამისად). თუ ჩვენ S-სა და R-ს შევაერთებთ D წყაროზე ისე რომ S = D და R = D'
მაშინ მივიღებთ ახალ ტრიგერს რომელიც D ტრიგერის სახელითაა ცნობილი. მას სხვანაირად
ასევე უწოდებენ: Data ტრიგერი, დაყოვნების flip-flop ან უბრალოდ D flip-flop.
D flip-flop ერთერთი უმნიშვნელოვანესი flip-flop არის ვინაიდან გამორიცხავს S = R 
მდგომარეობას.

>![Getting Started](./7.6.jpg)<br>
>**Fig 7.6 : Simple D latch**
## 7.2 **დ ლატჩი**
### 7.2.1 **უტაქტო**

განვიხილოთ D ლატჩის(NAND) ჭეშმარიტობის ცხრილი:
თუ D = 1, მაშინ RS ლატჩზე გვაქვს R = 0, S = 1 და გამოდის რომ Q = 1;<br>
თუ D = 0, მაშინ RS ლატჩზე გვაქვს R = 1, S = 0 და გამოდის რომ Q = 0.<br>
დ ლატჩი არ გამოიყენება რამდენადაც მისი ჭეშმარიტების ცხრილი პირდაპირ გამოდის
Q = D (ცხრილი 1).

>![Getting Started](./t7.1.jpg)<br>
>**ცხრილი 1**

### 7.2.2 **ტაქტიანი**
ჩვენ შეგვიძლია უტაქტო D ლატჩი ტაქტიანად შემდეგნაირად გადავაკეთოთ:
RS ლატჩში R = (D NAND CLK) და S = (D' NAND CLK). ტაქტის დაბალ მომენტში გვექნება
R = 1 და S = 1, RS(NAND) ლატჩში ეს მდგომარეობა არ იწვევს ცვლილებას შესაბამისად
არც ჩვენს ახალ D ლატჩში გვექნება არანირი ცვლილება. თუ ტაქტის მაღალი მომენტი გვაქვს, მაშინ გამოსასვლელის მნიშვნელობას D შესასვლელი აკონტროლებს — CLK = 1 და D = 1 მაშინ Q = 1,
თუ CLK = 1 და D = 0 -> Q = 0. გამარტივებული სახით რომ ჩავწეროთ, თუ გვაქვს ტაქტის
მაღალი მომენტი, მაშინ Q = D და თუ გვაქვს ტაქტის დაბალი მომენტი, მაშინ გამოსასვლელზე
ცვლილება არ გვაქვს. ჩვენი მიღებული ლატჩი არის ტრანსპარენტული სახის, რაც 
გულისხმობს იმას, რომ თუ ტაქტის მაღალი წყარო გვაქვს შემავალი სიგნალის ცვლილება
იწვევს გამოსასვლელზე დაუყოვნებელ ცვლილებას. (ცხრილი 2)

აქვე თანდართულია სიგნალების დიაგრამა, რაც უფრო თვალსაჩინოს გახდის ტაქტიანი D
ლატჩის მუშაობის პრინციპს.

>![Getting Started](./7.7.jpg =350x)<br>
>**Fig 7.7: a) D latch with clock. b) signal diagram for given ciruit**
>![Getting Started](./t7.2.jpg)<br>
>**ცხრილი 2**

##  7.3  **D FLIP-FLOP**

მიუხედავად იმისა , რომ ამდენად შევცვალეთ SR ლატჩი და მივიღეთ D ლატჩი
იგი მაინც არ არის სრულყოფილი, ვინაიდან ტაქტის მაღალ წყაროზე გამომავალი სიგნალი შემავალი სიგნალის ცვილილებასთან ერთად იცვლება. ზოგადად ტრანსპარენტული ლატჩები
გამოყენებადია, მაგრამ კომპიუტერულ წრედებსა და ლოგიკაში --- არა. იმისათვის, რომ D 
ლატჩი გამოყენებადი გახდეს უნდა შევცვალოთ ისე, რომ მან ინფორმაცია 
წინასწარ განსაზღვულ მომენტებში შეინახოს. 

**7.8** სურათზე ვხედავთ RC წრედს ტაქტის წყაროსთან. ეს სწორედ ის ცვლილებაა
რომელიც გვჭირდება ჩვენ, მაგრამ აუცილებელ პირობას წარმოადგენს, რომ ტაქტის სიგანე
გაცილებით დიდი უნდა იყოს, ვიდრე RC წრედის დროის კონსტანტა. თუ ყველაფერი
იდეალურადაა, ტაქტის მაღალ მომენტში კონდესატორი მთლიანად ახერხებს დამუხტვას. 
კონდესატორის დამუხტვისას გადის დენი, რომელიც თანდათან მცირდება და იგი წარმოქმინს ძაბვას 
რეზისტორზე. დამუხტვის შემდეგ კონდესატორი დენს აღარ ატარებს, ამიტომაც ძაბვა რეზისტორზე 
ხდება 0ვ.

>განვიხილოთ რამდენიმე შემთხვევა (იხილეთ ცხრილი 3):
>
>>1) CLK- = 0, CLK+ = 1 ანუ 0 -> 1.
რახან თავდაპირველი მდგომარეობა გვაქვს, ტაქტის დაბალ დონეზე შეგვიძლია ჩავთვალოთ
რომ კონდესატორი არის მთლიანად განმუხტული ანუ Vc = 0. მაღალ დონეზე გადასვლისას
კონდენსატორი დამუხტვას თავდაპირველად დიდი ტემპით იწყებს, რომელიც თანდათან
იკლებს და ეს ტემპი ფაქტობრივად დენის ძალა გამოდის. რადგან დროის კონსტანტა პატარა
არის დამუხტვა ხდება საკმაოდ სწრაფად, ანუ დენის ძალა გვაქვს მხოლოდ ცოტახნით.
დამუხტვის შემდეგ კონდესატორი დენს აღარ ატარებს, შესაბამისად რეზისტორზე ძაბვა 0-ის
ტოლი ხდება. თუ დავაკვირდებით რეზისტორზე ძაბვას მის გრაფიკზე დავინახავთ 
ერთეულოვან იმპულსს. სწორედ ამ ერთეულოვანი იმპულსისას იღებს D ლატჩი მნიშვნელობას.
>
>>2) CLK- = 1, CLK+ = 1 ანუ 1 -> 1.
ამ შემთხვევაში კონდესატორი დამუხტულია და დენს არ ატარებს, რადგან ტაქტის წყაროში
ცვლილება არ გვაქვს, შესაბამისად არ იცვლება ძაბვა რეზისტორზე და ლატჩზე ცვლილება
არ გვაქვს.
>
>>3) CLK- = 1, CLK+ = 0 ანუ 1 -> 0.
ამ შემთხვევაში კონდესატორი იწყებს განმუხტვას და რეზისტორზე ძაბვა იცვლება და
ხდება უარყოფითი, ამ შემთხვევაშიც არანაირი ცვლილება არ გვაქ ლატჩზე.
>
>>4) CLK- = 0, CLK+ = 0 ანუ 0 -> 0.
ანალოგიურია მე-2 პუნქტის, რადგან კონდესატორი გვაქ განმუხტული და წრედზე არ ვდებთ
მაღალ ძაბვას არ იმუხტება, ანუ რეზისტორზე ძაბვა არ იცვლება და შესაბამისად არ
გვაქ ცვლილება ლატჩის გამოსასვლელზეც.

იგივე შედეგის მისაღწევად მეორე გზაც არსებობს, რომელიც ნაკლებად გამოყენებადია, მაგრამ
ნაკლებ ფიზიკასაც მოითხოვს. ამ შემთხვევაში ძალიან მცირე მოდიფიკაციაა გასაკეთებელი
რომელიც არის AND GATE რომლის შესასვლელებიც არიან CLK და CLK-ის ინვერტირებული.
ამ დროს უნდა გავითვალისწინოთ რომ მაინვერტირებელს გააჩნია თავისი დაყოვნება
და მოგვიწევს კენტი რაოდენობის მაინვერტირებელის კასკადირება, რათა ძალიან მოკლე 
არ იყოს პულსის სიგანე.

>განვიხილოთ რამდენიმე შემთხვევა, A = CLK & B = CLK':
>
>>1) CLK- = 0, CLK+ = 1 ანუ 0 -> 1.
AND GATE-ის A შესასვლელი მყისიერად ასწრებს მნიშვნელობის ცვლილებას ხოლო B
შესასვლელი აგვიანებს ცვლილებას ინვერტორის გამო, რის გამოც გამომავალი სიგნალი
მყისიერად ხდება ლოგიკური 1 და მალევე ხდება ლოგიკური 0.
>
>>2) CLK- = 1, CLK+ = 1 ანუ 1 -> 1.
ამ შემთხვევაში ცვლილება არ გვაქვს შესასვლელებზე შესაბამისად არც გამოსასვლელზე.
>
>>3) CLK- = 1, CLK+ = 0 ანუ 1 -> 0.
ამ შემთხვევაში ერთ შესასვლელზე მყისიერად იცვლება და ხდება ლოგიკური 0 და
გამოსასვლელზე მყისიერად ხდება ლოგიკური 0.
>
>>4) CLK- = 0, CLK+ = 0 ანუ 0 -> 0.
ამ შემთხვევაში არ გვაქვს ცვლილება და შესაბამისად არ გვაქ ცვლილება 
გამოსასვლელზე.


>![Getting Started](./7.8.jpg)<br>
>**Fig.7.8 : a) D clocked latch with RC circuit. b) Signal diagram for given circuit.**

ამ ფიგურაზე კარგად ჩანს მოდიფიცირებული D ლატჩის, აწ უკვე D flip-flop მუშაობის
პრინციპი.

>![Getting Started](./t7.3.jpg)<br>
>**ცხრილი 3: ისრებით აღნიშნულია დონის ცვლილება.**

## 7.4 **EDGE TRIGGERING VS LEVEL CLOCKING**
როდესაც წრედი არის EDGE-TRIGGERRED იგი მნიშვნელობას იცვლის მხოლოდ ტაქტის
დონის ცვლილებისას, ხოლო როდესაც LEVEL-CLOCKED არის მაშინ მნიშვნელობის შეცვლა
შესაძლებელია მთლიანი დონის განმავლობაში.

## 7.5 **PRESET AND CLEAR**
Flip-flop-ის პირველი გამოყენებისას ისინი შემთხვევით მდგომარეობაში ირთვებიან.
იმისათვის რომ ზოგიერთი კომპიუტერი ჩაირთოს ოპერატორი უნდა დააწვეს მასტერ
ღილაკს გასუფთავებისთვის. ამ ღილაკზე დაწოლა ყველა flip-flop-ს ასუფთავებს,
ასევე ზოგიერთ შემთხვევაში გამოსადეგია მნიშვნელობების წინასწარ მინიჭება 
flip-flop-ებისთვის სანამ კომპიტუერი დაიწყებს მუშაობას. სურათზე(Fig 7.9) 
ნაჩვენებია თუ როგორ შეიძლება არსებულ D flip-flop-ში ამ ფუნქციონალის
შეტანა მარტივად. თუ Preset-ს დავაყენებთ 0-ზე მაშინ Q-ს მნიშვნელობა გახდება
1, ხოლო თუ Reset-ს დავაყენებთ 0-ზე მაშინ Q-s მნიშვნელობა გახდება 0.

>![Getting Started](./7.9.jpg)<br>
> **Fig 7.9 : D Flip-Flop with Preset and Reset**

Preset-სა და Reset-ს ხშირად "Direct Set" და "Direct Reset"-საც ეძახიან. 
პირდაპირი(Direct) გულისხმობს იმას რომ მათი შეცვლა იწვევს მყისიერ ცვლილებას
გამოსასვლელზე და არ არიან დამოკიდებულნი ტაქტის ცვლილებაზე. ამ ორ ფუნქციონალს ტაქტისა და ინფორმაციის წყაროზე უფრო მაღალი პრიორიტეტი აქვს ვიდრე ტაქტის წყარო ან თუნდაც 
ინფორმაციის წყარო. თუ ჩვენ წინასწარ დავსეტავთ მნიშვნელობას (Preset = 0,
Reset = 1) გამოსასვლელზე მივიღებთ ლოგიკურ 1-ს და ვერც ტაქტისა და ვერც შემავალი
სიგნალის ცვლილება ამას ვერ შეცვლის. ანალოგიურია ქცევა თუ დავარესეტებთ (Preset 
= 1, Reset = 0) გამოსასვლელზე მივიღებთ ლოგიკურ 0-ს და დარჩება ამ მდგომარეობაში.
თუ ორივე მნიშვნელობას 0-ზე დავაყენებთ მაშინ განუსაზღვრელი მდგომარეობა გვექნება
ვინაიდან ერთისმხრივ ვცდილობთ პარალელურ რეჟიმში თან წინასწარ დავსეტოთ 
მნიშვნელობა და თან დავარესეტოთ იგი, ან მეორენაირად შეგვიძლია შევხედოთ ამ 
სიტუაციას, RS ლატჩზე (0,0) მდგომარეობა გვაქ რომელიც აკრძალულია მისთვის.
ეს ყველაფერი უფრო თვალნათლად არის ასახული ცხრილ 4-ში.

> ![Getting Started](./t7.4.jpg) <br>
> **ცხრილი 4**

ინტეგრირებული წრედები არ იყენებენ RC წრედს რადგან კონდენსატორის ჩიპზე განთავსება რთულია 
ამიტომაც იყენებენ სხვანაირ დიზაინს როგორიც არის მოცემული 
Fig 7.11-ში. როგორც ვხედავთ მთლიან წრედში გამოყენებულია 3 SR NAND ლატჩით.
მთლიანი წრედი შეგვიძლია ორ ნაწილად გავყოთ: ***მიღების ნაწილი*** ,რომელიც 
მარცხენა მხარეს მდებარე ორ ლატჩს მოიცავს და ***პასუხის ნაწილი***, მარჯვნივ 
მდებარე ლატჩი. თუ ტაქტი დაბალ დონეზე არის მაშინ მიღების ნაწილიდან ორივე
გამომავალი  სიგნალი არის ლოგიკური 1, და ***პასუხის ნაწილი*** არ იცვლება.
თუ ტაქტი გადადის მაღალ დონეზე, მაშინ მხოლოდ ერთი მარცხენა ლატჩი გამოსცემს 0-ს
,რაც დამოკიდებულია D-ს მნიშვნელობაზე და სეტავს/არესეტებს გამომავალ სიგნალს.
თუ D = 0 მაშინ ქვედა მარცხენა ლატჩიდან გამომავალი სიგნალი გადადის 0-ზე, თუ
D = 1 მაშინ ზედა. თუ ტაქტი რჩება მაღალ დონეზე მაშინ ***მიღების ნაწილი***
რჩება მუდმივი და შესაბამისად არ აძლევს ***პასუხის ნაწილს*** საშუალებას რომ
შეიცვალოს. <br>
***მიღების ნაწილი*** აფიქსირებს ტაქტის დაბალი სიგნალიდან მაღალზე გადასვლას
და მხოლოდ ამის შემდეგ აძლევს უფლებას ***პასუხის ნაწილს*** რომ შეინახოს არსებული
D მნიშვნელობა.

> ![Getting Started](./7.11.jpg) <br>
> **Fig 7.10 D Flip-Flop as integrated circuit**

წინა წრედის მოდიფიკაციას წარმოადგენს შემდეგი წრედი ,Fig 7.11-ში მოცემული.
ამ წრედს დამატებული აქვს Preset & Reset ფუნქციონალი და ორივე ინტეგრირებული
წრედი ზუსტად ისე იქცევა როგორც RC წრედით იმპლემენტირებული წრედები.

> ![Getting Started](./7.10.jpg) <br>
> **Fig 7.11 D Flip-Flop as integrated circuit with Preset and Reset**

>D flip-flop უმეტესად გამოიყურება შემდეგნაირად:<br>
> ![Getting Started](./7.12.jpg) <br>
> **Fig 7.12 D Flip-Flop logic design**<br>
> პატარა სამკუთხედი აღნიშნავს ტაქტის შესასვლელს, პატარა ბურთები PR და CLR-სთან
> აღნიშნავს რომ საჭიროა დაბალი ინფუთი(ინვერტირებულ შესასვლელებზე) ამ შესასვლელებზე რათა შესაბამისი 
> ფუნქციონალი ამოქმედდეს. თუ პატარა ბურთი არ აქვს შესასვლელს მაშინ ფუნქციონალი
> ჩვეულებრივ გამოიძახება როცა შემავალი სიგნალი მაღალია.

## 7.6 [**დროები**](https://en.wikipedia.org/wiki/Flip-flop_(electronics)#Timing_considerations)

დიოდებსა და ტრანზისტორებს სჭირდებათ გარკვეული დრო სანამ ისინი ამოქმედბიან ან
სანამ ერთი მდგომარეობიდან მეორე მდგომარეობაში გადავლენ. ბიპოლარუ დიდებისთვის
და ტრანზისტორებისთვის ეს გადართვის დროები ნანოწამებია.

### **გავრცელების დაყოვნების დრო(Propagation Delay Time  t<sub>p</sub>)**

სწორედ გადართვის დრო არის მიზეზი იმისა რომ არსებობს გავრცელების დაყოვნება.
ის დრო ,რაც საჭიროა რომ flip-flop-მა ან Gate-მა შეცვალოს გამომავალი სიგნალი
არის სწორედ გავრცელების დაყოვნების დრო. მაგალითად თუ D flip-flop-ს გავრცელების
დაყოვნების დრო აქვს 10 ნანო წამი, მაშინ ტაქტის მაღალ დონეზე გადასვლიდან 10 ნანო
წამი სჭირდება flip-flop-ს რომ გამოსასვლელზე ასახოს D-ს მნიშვნელობა.<br>
ზოგადად  t<sub>p</sub> არის საკმაოდ პატარა და შეგვიძლია არ გავითვალისწინოთ, მაგრამ თუ
საქმე გვაქ საკმაოდ ჩქარ წრედებთან მაშინ გასათვალისწინებელია ის ფაქტი რომ თუ
  t<sub>p</sub> = 10 ნწმ, 10 ნანო წამია საჭირო რათა მოხერხდეს ცვლილება და საჭირო
 ფუნქციონალის შესრულება, მაგალითად სხვა წრედის გააქტიურება.

### **მოწყობის დრო(Setup Time  t<sub>setup</sub>)**

პარაზიტული ტევადობა (Stray Capacitance) და სხვა ფაქტორები საჭიროს ხდიან
რომ D-ს მნიშნველობა იმაზე ადრე განისაზღვროს ვიდრე ტაქტი დაბალიდან მაღალ დონეზე
ავა. t<sub>setup</sub> არის ის საჭირო დრო, რა დროით ადრეც უნდა განისაზღვროს შემავალი
მნიშვნელობა სანამ ტაქტის მაღალ დონეზე ავა.<br>
თუ t<sub>setup</sub> = 15 ნწმ, მაშინ D-ს საბოლოო ცვლილებიდან 15 ნანოწამის შემდეგ
მომხდარ პირველ ტაქტის დადებით ცვლილებაზე(დაბალიდან მაღალზე) აისახება პასუხი.
თუ მაგალითად შემავალი სიგნალი ტაქტის დადებით ცვლილებამდე 5 ნანოწამით ადრე 
შევცვალეთ, გამოსასვლელზე შესაძლოა სწორი პასუხი ვერ მივიღოთ.

### **შეჩერების დრო(Hold Time t<sub>hold</sub>)**

იმისათვის რომ გამოსასვლელზე დადგეს პასუხი საჭიროა რომ შემავალი სიგნალი
გარკვეული დროით დაყოვნდეს მას შემდეგ რაც ტაქტის დადებითი ცვლილება მოხდება.
შეჩერების დრო სწორედ ამ დროის მინიმალური მნიშვნელობა არის.<br>
მაგალითად D flip-flop-ის შეჩერების დრო არის 5 ნანო წამი. მაშინ ტაქტის დადებითი
ცვლილებიდან 5 ნანოწამის განმავლობაში უნდა დაყოვნდეს შემავალი სიგნალი რათა
გამომავალ სიგნალზე შესაბამისი მნიშვნელობა დადგეს.

## 7.7 **D Flip-Flop შეერთებები**

### 7.7.1 **Master-Slave D Flip-Flop**

ჩვენ შეგვიძლია ორი D Flip-Flopi შევაერთოთ ისე როგორც ნაჩვენებია Fig.13-ზე.
პირველი(მარცხენა) ტრიგერის გამოსასვლელი წარმოადგენს მეორე ტრიგერის შესასვლელს
ხოლო ტაქტები ერთმანეთის ინვერტირებულია. როგორც ვიცით D ტრიგერი ტაქტის დადებით
ცვლილებაზე რეაგირებს, ამ შეერთებაში კი თუ დავაკვირდებით Master ტრიგერი ანალოგიურად
დადებით ცვლილებაზე რეაგირებს ხოლო Slave ტრიგერი უარყოფით ცვლილებაზე. თუ სიმულაციას
გავაკეთებთ დავინახავთ რომ საბოლოო პასუხის მიღებას სჭირდება ერთი მთლიანი ტაქტი, იგულისხმება
ტაქტის დადებითი და უარყოფითი ცვლილება. თუ შესასვლელზე დავაყენებთ ლოგიკურ 1-ს
ტაქტის მაღალ ცვლილებაზე პირველი ტრიგერი გადაირთობა და მის გამოსასვლელზე დადგება 1.
ამ დროს მარჯვენა ტრიგერზე ცვლილება არ გვაქვს რადგან მასთან ტაქტი დაბალ დონეზეა. მარჯვენა
ტრიგერი იმახსოვრებს 1-ს, და ტაქტის უარყოფით ცვლილებაზე არ რეაგირებს. ამ დროს ირთვება
მარჯვენა ტრიგერი, რომლის შესასვლელზეც ლოგიკური 1 დგას და ტაქტს დადებითი ცვლილება აქვს და
ისიც იმახსოვრებს გამოსასვლელზე ლოგიკურ 1-ს. შესაბამისად საბოლოო გამოსასვლელზე პასუხის
მიღებას სჭირდება ტაქტის ჯერ დადებითი ხოლო შემდეგ უარყოფითი ცვლილება. უნდა აღინიშნოს
ის ფაქტი, რომ ტაქტის ცვლილებებს შორის ინფუთის ცვლილება არ იწვევს არანირ სხვაობას ერთი
ტაქტის განმავლობაში.

> ![Getting Started](./7.13.jpg) <br>
> **Fig 7.13 D Flip-Flop Master-Slave connection**<br>

### 7.7.1 **Falling Edge D Flip-Flop**

თუ ტაქტის წყაროს D ტრიგერთან ინვერტირებულად მივაერთებთ მივიღებთ ახალ D ტრიგერს
რომელიც მხოლოდ ტაქტის უარყოფით ცვლილებაზე(მაღლიდან დაბალზე) რეაგირებს.

>![Getting Started](./7.14.jpg) <br>
> **Fig 7.14 Falling Edge D Flip-Flop**<br>

### 7.7.1 **Dual Edge D Flip-Flop**

Fig 7.15-ში ნაჩვენებია თუ როგორ შეიძლება ავაგოთ ისეთი ტრიგერი რომელიც ტაქტის
ნებისმიერ ცვლილებაზე ახდენს რეაგირებას. ამისთვის გამოვიყენეთ 2 D ტრიგერი და 
მულტიპლექსორი. მარტივად გავიაროთ რა ხდება მოცემულ წრედში. როდესაც ტაქტის
დადებითი ცვლილება გვაქ (0-დან ადის 1-ზე) ქვედა ტრიგერი იმახსოვრებს შემოსულ
მნიშვნელობას, და უკვე მულტიპლექსორის ასარჩევ ფეხზე მიდის ლოგიკური 1, რომელიც
აიძულებს მულტიპლექსორს მის ქვემოთა შესასვლელზე არსებული მდგომარეობა გამოიტანოს.
მომდევნო უარყოფით ცვლილებაზე კი ზედა ტრიგერის მიიღებს მნიშვნელობას, და რადგან 
ტაქტის ცვლილება უარყოფითია მულტიპლესქორის ასარჩევ ფეხზე მიდის 0, რომელიც აიძულებს
მას პირველ შესასვლელზე არსებული მდგომარეობა გამოიტანოს.<br>
მთელი იდეა ამ წრედის არის ის რომ მულტიპლექსორმა აჩვენოს ახლად შეცვლილი
ტრიგერის მნიშვნელობა. ტაქტის თითო ცვლილებაზე მხოლოდ ერთ ტრიგერს შეუძლია
მნიშვნელობის შეცვლა და მულტიპლექსორითაც შესაბამისად ვირჩევთ რომელი შესასვლელი
გამოიტანოს საბოლოო მნიშვნელობად.

>![Getting Started](./7.15.jpg) <br>
> **Fig 7.15 Falling Edge D Flip-Flop**<br>

## 7.8 [**გამოყენება**](https://www.electronicshub.org/flip-flop-applications/)

როგორც უკვე არაერთხელ ვახსენეთ D ტიპის ტრიგერი საკმაოდ მნიშვნელოვანია
რამდენადაც არ აქვს აკრძალული მდგომარეობა (გარდა Preset = Reset = 0) შემთხვევისა 
და D ტრიგერის გამოყენების არეალს შეადგენს სიხშირის გამყოფი (Frequency Divider).
თუ ჩვენ Q'-ს შევიყვანთ D-ს მნიშვნელობად მაშინ გამომავალი სიგნალს ექნება შემავალი
სიგნალის სიხშირის ნახევარი (Fig 7.16).

>![Getting Started](./7.16.jpg) <br>
> **Fig 7.16 D Flip-Flop as Frequency Divider**<br>

ერთ-ერთი უმნიშვნელოვანესი დატვირთვა, რაც აქვთ ზოგადად D flip-flop-ებს
არის მეხსიერებასთან დაკავშირებული. ისინი წარმოადგენენ რეგისტრების საბაზისო ერთეულებს.
სულ რაღაც 4 D ტრიგერის გადაბმით შესაძლებელია 4 ბიტიანი ელემენტარული მეხსიერების
იმპლემენტირება (Fig. 7.17), რომელიც მინიჭებულ მნიშვნელობას მხოლოდ ტაქტის მაღალ ცვლილებაზე
ინახავს.

>![Getting Started](./7.17.jpg) <br>
> **Fig 7.17 4 Bit Buffer Register**<br>

უფრო დახვეწილ ვერსიას წარმოადგენს შემდეგი წრედი, სადაც დამატებით გვაქვს CLR(Reset მაშინ
როცა, მასში შემავალი სიგნალი მაღალია) და LOAD. თუ CLR = 1 მაშინ შენახული ინფორმაცია
სუფთავდება, ხოლო, როდესაც CLR 0-ის ტოლია, შესაძლებელია ინფორმაციის ჩაწერა. როცა LOAD = 0 x ბიტები
ვერ აღწევენ ტრიგერებამდე. ამავდროულად LOAD' = 1 და ამ დროს თითოეული ტრიგერის
შესასვლელზე ხვდება მისი გამოსასვლელი. თუ LOAD = 1 მაშინ x-ების მნიშვნელობები აღიბეჭდება
შესაბამისი ტრიგერების გამოსასვლელებზე.

>![Getting Started](./7.18.jpg) <br>
> **Fig 7.17 4 Bit Controlled Buffer Register**<br>

D Flip-Flop-ები გამოიყენება Shift Registers(წანაცვლებადი რეგისტრის) ასაგებად (Fig. 7.19). შიფტ რეგისტრი
ტაქტის ყოველ დადებით ცვლილებაზე ერთით მარჯვნივ ან მარცხნივ გადაწევენ დამახსოვრებულ
ბიტებს. Fig. 7.19-ზე ნაჩვენებია მარცხნივ ერთით წამნაცვლებელი.

>![Getting Started](./7.19.jpg) <br>
> **Fig 7.17 Shift Left Register**<br>