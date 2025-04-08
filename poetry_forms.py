poetry_forms = {
    "English": {
        "Haiku": {"syllables": [5, 7, 5], "lines": 3},
        "Sonnet": {"syllables": [10] * 14, "lines": 14},  # Iambic pentameter, 10 syllables per line
        "Limerick": {"syllables": [8, 8, 5, 5, 8], "lines": 5}
    },
    "Chinese": {
        "Jueju": {"syllables": [5, 5, 7, 7], "lines": 4},  # 5 or 7 syllables, regulated tone
        "Lüshi": {"syllables": [5] * 8, "lines": 8},      # 5 or 7 syllables, strict parallelism
        "Ci": {"syllables": "variable", "lines": "variable"}  # Depends on tune pattern
    },
    "Japanese": {
        "Haiku": {"syllables": [5, 7, 5], "lines": 3},
        "Tanka": {"syllables": [5, 7, 5, 7, 7], "lines": 5},
        "Senryu": {"syllables": [5, 7, 5], "lines": 3}
    },
    "Indian": {  # Sanskrit and regional traditions
        "Shloka": {"syllables": [8, 8], "lines": 2},  # Typically 8 syllables per half-line, epic form
        "Ghazal": {"syllables": "variable", "lines": 10},  # Urdu influence, 5+ couplets
        "Doha": {"syllables": [13, 11], "lines": 2}  # Hindi/Prakrit, syllable split per line
    },
    "Vietnamese": {
        "Luc Bat": {"syllables": [6, 8] * 3, "lines": 6},  # Alternating 6 and 8, extensible
        "Song That": {"syllables": [7] * 4, "lines": 4},  # 7 syllables, folk style
        "Cach Dieu": {"syllables": "variable", "lines": 4}  # Regulated, varies by tone
    }
}
