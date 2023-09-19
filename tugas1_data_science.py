#!/usr/bin/env python
# coding: utf-8

# # Week 1 Review Exercises
# 
NAMA :Resti Ajeng Sutiani
NIM  : E1E121039
# Q1. Data Types
# 
# What is the data type of the variable `pop`?

# In[1]:


pop = 5.8


# In[23]:


print(type(pop))


# Q2. Which of the following is a valid variable name of of population below 15 years old?
# 

# In[3]:


# which line won't give an error? Comment out the ones that do!
15_years_and_below = 12.33
get_ipython().run_line_magic('_pop_15_below', '= 12.33')
_15&below_pop = 12.33
_15_below_pop = 12.33


# In[ ]:


15_years_and_below = 12.33


# In[22]:


_15_below_pop = 12.33


# Q3. What will be stored in `result`?

# In[24]:


result = 3 + 4 ** 2 - (5 // 2)


# In[25]:


print(result)


# Q4. If Singapore has an estimated population of 5.85 million and the land area is 700 square kilometers, what is the population density (number of people per KM)? 
# 

# In[34]:


# Estimated total Population of Singapore, in millions
total_pop_millions = 5.85

# Total land area, in KM
land_area = 700

# How many people are there per KM?
people_per_KM = 5850000 / 700
print(people_per_KM s)


# Q5. Write a function called `pop_density()` that receives two arguments:
# 1. the population, recorded in millions, `population_mil`
# 2. the land area, in square kilometres, `land_area_sqkm`
# 
# The function should calculate and return the population density. 
# 

# In[30]:


# Write the function here
def pop_density(population_mil, land_area_sqkm):
    density = population_mil * 1_000_000 / land_area_sqkm
    return density

population_mil = 5.85  
land_area_sqkm = 700   

kepadatan = pop_density(population_mil, land_area_sqkm)
print(f"Kepadatan penduduk adalah {kepadatan:.2f} orang per kilometer persegi.")


# Q6. Call the function you have written to calculate and display the population density of Hong Kong: 7.50 million people in a land area of 1050 km squared 
# 

# In[35]:


# Call the function 
# Memanggil fungsi pop_density() dengan data Hong Kong
population_mil = 7.50  
land_area_sqkm = 1050 

# Menghitung kepadatan penduduk Hong Kong dengan memanggil fungsi
kepadatan = pop_density(population_mil, land_area_sqkm)

# Menampilkan hasil kepadatan penduduk Hong Kong
print(f"Kepadatan penduduk Hong Kong adalah {kepadatan:.2f} orang per kilometer persegi.")


# Q7. Using the `pop_density()` function, calculate the population density of Singapore and then use comparison operators to compare the population densities of Singapore and Hong Kong.
# 
# Singapore's population: 5.85 million
# Singapore's land area: 700 sq km
# 
# (Data From [Worldometers](http://worldometers.info))
# 

# In[36]:


# use the function
# Data Singapura
penduduk_singapura = 5.85  # Jumlah penduduk Singapura dalam jutaan
luas_daratan_singapura = 700  # Luas daratan Singapura dalam kilometer persegi

# Data Hong Kong
penduduk_hongkong = 7.50  # Jumlah penduduk Hong Kong dalam jutaan
luas_daratan_hongkong = 1050  # Luas daratan Hong Kong dalam kilometer persegi

# Menghitung kepadatan penduduk Singapura dan Hong Kong menggunakan fungsi pop_density()
kepadatan_singapura = pop_density(penduduk_singapura, luas_daratan_singapura)
kepadatan_hongkong = pop_density(penduduk_hongkong, luas_daratan_hongkong)

# compare hk vs sg population density 
# Membandingkan kepadatan penduduk Singapura dan Hong Kong
if kepadatan_singapura > kepadatan_hongkong:
    print("Kepadatan penduduk Singapura lebih tinggi daripada Hong Kong.")
elif kepadatan_singapura < kepadatan_hongkong:
    print("Kepadatan penduduk Hong Kong lebih tinggi daripada Singapura.")
else:
    print("Kepadatan penduduk Singapura dan Hong Kong sama.")


# Q8. Let's add another area to compare: Macao's population is 0.65 million in a land area of 30 sq km. Find out whether Singapore's population density is higher than BOTH Hong Kong and Macao.

# In[37]:


# Calculate Macao's density (use the function!)
# Data Singapura
penduduk_singapura = 5.85  # Jumlah penduduk Singapura dalam jutaan
luas_daratan_singapura = 700  # Luas daratan Singapura dalam kilometer persegi

# Data Hong Kong
penduduk_hongkong = 7.50  # Jumlah penduduk Hong Kong dalam jutaan
luas_daratan_hongkong = 1050  # Luas daratan Hong Kong dalam kilometer persegi

# Data Macao
penduduk_macao = 0.65  # Jumlah penduduk Macao dalam jutaan
luas_daratan_macao = 30  # Luas daratan Macao dalam kilometer persegi

# Menghitung kepadatan penduduk Singapura, Hong Kong, dan Macao menggunakan fungsi pop_density()
kepadatan_singapura = pop_density(penduduk_singapura, luas_daratan_singapura)
kepadatan_hongkong = pop_density(penduduk_hongkong, luas_daratan_hongkong)
kepadatan_macao = pop_density(penduduk_macao, luas_daratan_macao)

# Singapore's population density is higher than both Hong Kong AND Macao
# Mengecek apakah kepadatan penduduk Singapura lebih tinggi daripada Hong Kong dan Macao
if kepadatan_singapura > kepadatan_hongkong and kepadatan_singapura > kepadatan_macao:
    print("Kepadatan penduduk Singapura lebih tinggi daripada Hong Kong dan Macao.")
else:
    print("Kepadatan penduduk Singapura tidak lebih tinggi daripada Hong Kong dan Macao.")


# Q9. Write a function called compare_density() that receives two arguments representing the population densities of two areas. The function will compare the two values and print one of the following strings:
# - “Area 1 has higher density”
# - “Area 2 has higher density”
# - “Both areas have the same density”

# In[40]:


# Write the function
def compare_density(kepadatan_area1, kepadatan_area2):
    """
    Fungsi ini membandingkan dua kepadatan penduduk dari dua area dan mencetak hasil perbandingan.

    Parameters:
    - kepadatan_area1 (float): Kepadatan penduduk area pertama.
    - kepadatan_area2 (float): Kepadatan penduduk area kedua.

    Returns:
    - None
    """
    if kepadatan_area1 > kepadatan_area2:
        print("Area 1 memiliki kepadatan lebih tinggi.")
    elif kepadatan_area1 < kepadatan_area2:
        print("Area 2 memiliki kepadatan lebih tinggi.")
    else:
        print("Kedua area memiliki kepadatan yang sama.")

# Contoh penggunaan fungsi
kepadatan_area1 = 100  # Ganti dengan nilai kepadatan area pertama
kepadatan_area2 = 120  # Ganti dengan nilai kepadatan area kedua


# Then we can test the function by passing the values of `kepadatan_area1` and `kepadatan_area2` as arguments.

# In[39]:


compare_density(kepadatan_area1, kepadatan_area2)


# Q10. What will be the result of the following loop?
# 
# ```
# for year in range(2022, 2031, 2):
#     print(year)
# ```

# In[41]:


# Type in the code for the loop given above and execute to check your answer
for year in range(2022, 2031, 2):
    print(year)


# Q.11 Write a function projected_population() that receives three arguments:
# - Current population, in millions
# - Growth rate
# - Current year
# 

# The function should:
# - set the projected population to the current population
# - set the projected year to the current year
# - calculate the difference between the projected population and current population
# 
# while the difference is between -1 and 1:
# 1. print the projected year and the projected population
# 2. calculate the projected population = projected population + projected population * growth rate / 100
# 3. update the projected year 
# 4. recalculate the difference between the projected propulation and current population

# In[56]:


def projected_population(populasi_sekarang, tingkat_pertumbuhan, tahun_sekarang):
    # complete the function according to the guide
    # Inisialisasi proyeksi populasi dan tahun proyeksi
    proyeksi_populasi = populasi_sekarang
    tahun_proyeksi = tahun_sekarang

    # Menghitung selisih antara proyeksi populasi dan populasi saat ini
    selisih = proyeksi_populasi - populasi_sekarang

    # Selama selisih berada di antara -1 dan 1, teruskan perhitungan
    while -1 < selisih < 1:
        # Cetak tahun dan proyeksi populasi saat ini
        print(f"Tahun {tahun_proyeksi}: {proyeksi_populasi:.2f} juta")

        # Hitung proyeksi populasi berdasarkan tingkat pertumbuhan
        proyeksi_populasi = proyeksi_populasi + (proyeksi_populasi * tingkat_pertumbuhan / 100)

        # Perbarui tahun proyeksi
        tahun_proyeksi += 1

        # Hitung ulang selisih
        selisih = proyeksi_populasi - populasi_sekarang

# Contoh penggunaan fungsi
populasi_sekarang = 5.85  # Ganti dengan populasi saat ini dalam jutaan
tingkat_pertumbuhan = 2.0  # Ganti dengan tingkat pertumbuhan dalam persen per tahun
tahun_sekarang = 2023  # Ganti dengan tahun saat ini

projected_population(populasi_sekarang, tingkat_pertumbuhan, tahun_sekarang)


# In[57]:


# testing with Thailand
print("Proyeksi Pertumbuhan Populasi Thailand")
projected_population(populasi_sekarang=69.8, tingkat_pertumbuhan=0.3, tahun_sekarang=2020)


# Q.12 Write a function called `string_info()` which takes in a string argument and returns four values:
# - the first 3 characters
# - last 3 characters
# - the number of characters in the string
# - the string with each word capitalized

# In[65]:


def string_info(word):
    # Mendapatkan tiga karakter pertama dari kata
    karakter_pertama = word[:3]

    # Mendapatkan tiga karakter terakhir dari kata
    karakter_terakhir = word[-3:]

    # Menghitung jumlah karakter dalam kata
    jumlah_karakter = len(word)

    # Mengonversi kata dengan huruf besar di awal
    kata_huruf_besar = word.capitalize()

    # Mengembalikan hasil dalam bentuk tuple
    return karakter_pertama, karakter_terakhir, jumlah_karakter, kata_huruf_besar



# In[66]:


#calling the function
start, end, num, title = string_info("data science")

# Mencetak nilai yang dikembalikan oleh fungsi
print("Tiga karakter pertama:", start)
print("Tiga karakter terakhir:", end)
print("Jumlah karakter dalam kalimat:", num)
print("Kalimat dengan huruf besar di awal setiap kata:", title)



# In[67]:


# print what's returned
print(string_info("data science"))


# # Congratulations! 
# 
# You have reached the end of this notebook! Hope you have been able to practice and review the fundamental concepts in Python coding and we will do more next week!
