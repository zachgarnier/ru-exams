// TEMPLATE (ignored by the app). Copy to exams/a1-3.js (or a2-3.js), edit, then add "a1-3" to exams/manifest.js.
// Rules: in every "o" list the FIRST option is the correct one (shuffled at runtime).
// Strings can be bilingual: "english||français". Strings without "||" are shown as-is (use for Russian).
// vg items: {"k":"v"} vocabulary, {"k":"g"} grammar. reading items point to "texts" by index "t"; add "k":"tf" for true/false.
// listening items: "say" is the Russian audio text (run make_audio.py afterwards).
(window.EXAMS=window.EXAMS||[]).push({"id":"a1-3","level":"A1","title":"Exam 3 · Title||Examen 3 · Titre",
"texts":["Русский текст."],
"vg":[{"k":"v","q":"дом","o":["house||maison","street||rue","table||table","city||ville"]},
{"k":"g","q":"Я живу ___ Москве.","o":["в","на","из","к"]}],
"reading":[{"t":0,"k":"tf","q":"Это текст.","o":["True||Vrai","False||Faux"]}],
"listening":[{"say":"Здравствуйте!","q":"What is it?||Qu'est-ce que c'est ?","o":["A greeting||Une salutation","A goodbye||Un au revoir"]}]});
