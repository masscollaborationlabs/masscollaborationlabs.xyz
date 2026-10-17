/*
Website source code of Mass Collaboration Labs

Copyright (C) 2026 Mass Collaboration Labs

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
const copyrightYear = document.getElementById("copyright-year");
const languageToggle = document.getElementById("language-toggle");
const description = document.querySelector('meta[name="description"]');
const socialDescription = document.querySelector('meta[property="og:description"]');
const video = document.querySelector(".video-frame iframe");

if (copyrightYear) {
  copyrightYear.textContent = String(new Date().getFullYear());
}

if (languageToggle) {
  const translations = {
    tr: {
      description: "Mass Collaboration Labs: paylaşmanın ötesinde, yazılım dünyasını özgürleştirme hedefi. Çalışmalarımızı ve videolarımızı keşfedin.",
      socialDescription: "Paylaşmanın ötesinde, yazılım dünyasını özgürleştiriyoruz. Çalışmalarımızı ve videolarımızı keşfedin.",
      videoTitle: "Mass Collaboration Labs tanıtım videosu",
      languageLabel: "Sayfa dilini değiştir",
      navLabel: "Ana bağlantılar",
      logoAlt: "Mass Collaboration Labs logosu"
    },
    en: {
      description: "Mass Collaboration Labs: beyond sharing, liberating the software world. Discover our work and videos.",
      socialDescription: "Beyond sharing, liberating the software world. Discover our work and videos.",
      videoTitle: "Mass Collaboration Labs introduction video",
      languageLabel: "Change page language",
      navLabel: "Main links",
      logoAlt: "Mass Collaboration Labs logo"
    }
  };

  const setLanguage = (language) => {
    const translation = translations[language];
    const languageKey = language[0].toUpperCase() + language.slice(1);
    document.documentElement.lang = language;
    languageToggle.textContent = language === "tr" ? "English" : "Türkçe";
    languageToggle.setAttribute("aria-label", translation.languageLabel);

    document.querySelectorAll("[data-tr][data-en]").forEach((element) => {
      element.textContent = element.dataset[language];
    });

    if (description) {
      description.content = translation.description;
    }
    if (socialDescription) {
      socialDescription.content = translation.socialDescription;
    }
    if (video) {
      video.title = translation.videoTitle;
    }

    const navigation = document.querySelector(".primary-links");
    if (navigation) {
      navigation.setAttribute("aria-label", translation.navLabel);
    }
    document.querySelectorAll(".brand-logo").forEach((logo) => {
      logo.alt = translation.logoAlt;
    });
    document.querySelectorAll("[data-aria-tr][data-aria-en]").forEach((element) => {
      element.setAttribute("aria-label", element.dataset[`aria${languageKey}`]);
    });
    document.querySelectorAll("[data-alt-tr][data-alt-en]").forEach((image) => {
      image.alt = image.dataset[`alt${languageKey}`];
    });
  };

  let language = "tr";
  setLanguage(language);
  languageToggle.hidden = false;
  languageToggle.addEventListener("click", () => {
    language = language === "tr" ? "en" : "tr";
    setLanguage(language);
  });
}
