#girisYapildi = False
girisYapildi = True

kurslar = [
  "Yazılım Geliştirici Yetiştirme Kampı (C#)",
  "Yazılım Geliştirici Yetiştirme Kampı (JAVA)",
  "Yazılım Geliştirici Yetiştirme Kampı (JAVASCRİPT)",
  "Yazılım Geliştirici Yetiştirme Kampı (JAVA + REACT)",
  "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)",
  "Algoritma ve Programlamaya Giriş"
]


def kurslari_Listele():
  for kurs in kurslar:
    print(kurs)


benim_kurslarim = [
  "Yazılım Geliştirici Yetiştirme Kampı (C#)",
  "Yazılım Geliştirici Yetiştirme Kampı (JAVA)",
  "Algoritma ve Programlamaya Giriş"
]


def benim_kurslarimi_Listele():
  for kurs in benim_kurslarim:
    print(kurs)


if girisYapildi:
  benim_kurslarimi_Listele()
else:
  kurslari_Listele()
