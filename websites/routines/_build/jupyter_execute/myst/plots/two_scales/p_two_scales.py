#!/usr/bin/env python
# coding: utf-8

# # Plotting two scales
# 
# ## One plot
# 
# In this section, we will plot the female shares and the genre share for each year. We will plot these values in two scales graph, where the left y-axis is female share and the right x-axis is the genre share. 
# 
# Firs, we create a list with all the genres that we have use to categorize the fiction books.
# ```{code-block}
# fics = [
#         'Action/Adventure', 
#         'Childrens Stories', 
#         'Fantasty/Sci-Fi', 
#         'Horror/Paranormal', 
#         'Mystery/Crime',
#         'Romance', 'Suspence', 
#         'Spy/Politics', 
#         'Literary_1'
#         ]
# ```
# 
# To plot the two scales, we did a unique figure with all the genres and other figures with individual genres. The first code creates the figure with all the grapphs together.
# 
# ```{code-block}
# i1 = 0 
# i2 = 0
# fig, axs = plt.subplots(3, 3, constrained_layout=True)
# 
# for f in fics:
#     df1 = pf.subg_female_share(g = f)
#     df2 = pf.subgenre_share(g = f)
#     #define colors to use
#     col1 = 'g'
#     col2 = 'b'
# 
#     #define subplots
#     #add first line to plot
#     axs[i1][i2].plot(df1.year, df1.fs, color=col1)
# 
#     #add x-axis label
#     if (i2 == 1) & (i1 == 2):
#         axs[i1][i2].set_xlabel('Year', fontsize=10)
# 
#     #add y-axis label
#     if (i2 == 0) & (i1 == 1):
#         axs[i1][i2].set_ylabel('Female Share', color=col1, fontsize=10)
# 
#     #define second y-axis that shares x-axis with current plot
#     ax2 = axs[i1][i2].twinx()
# 
#     #add second line to plot
#     ax2.plot(df2.year, df2.fs, color=col2)
# 
#     #add second y-axis label
#     if (i2 == 2) & (i1 == 1):
#         ax2.set_ylabel('Genre Share', color=col2, fontsize=10)
#     axs[i1][i2].set_title(f, fontsize=10)
#     i2 = i2 + 1
#     if i2 == 3:
#         i2 = 0
#     else: 
#         pass
#     if i2 == 0:
#         i1 += 1
#     else:
#         pass
#         
# plt.suptitle('Two scales graphs')
# os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/shares/loc/two_scale')
# plt.savefig('p_2sca.png')
# plt.close()
# ```
# 
# This will produce the following figure
# ```{figure} ../../../images/two_scales/p_2sca.png
# :name: figure-example
# ```
# 
# ## Separated plots
# 
# The following, plots a figure for each fiction genre. 
# 
# ```{code-block}
# fics = [
#         'Action/Adventure', 
#         'Childrens Stories', 
#         'Fantasty/Sci-Fi', 
#         'Horror/Paranormal', 
#         'Mystery/Crime',
#         'Romance', 'Suspence', 
#         'Spy/Politics', 
#         'Literary_1'
#         ]
# 
# for f in fics:
#     df1 = pf.subg_female_share(g = f)
#     df2 = pf.subgenre_share(g = f)
# 
#     fig, axs = plt.subplots()
#     #define colors to use
#     col1 = 'g'
#     col2 = 'b'
# 
#     #define subplots
#     #add first line to plot
#     axs.plot(df1.year, df1.fs, color=col1)
# 
#     #add x-axis label
#     axs.set_xlabel('Year', fontsize=10)
# 
#     #add y-axis label
#     axs.set_ylabel('Female Share', color=col1, fontsize=10)
# 
#     #define second y-axis that shares x-axis with current plot
#     ax2 = axs.twinx()
# 
#     #add second line to plot
#     ax2.plot(df2.year, df2.fs, color=col2)
# 
#     #add second y-axis label
#     ax2.set_ylabel('Genre Share', color=col2, fontsize=10)
#     axs.set_title(f, fontsize=10)
#     os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/shares/loc/two_scale')
#     plt.savefig('p_2sca_'+f.replace('/','_').replace(' ','_')+'.png')
#     plt.close()
# ```
# 
# This will produce the following figure for all the fiction genres. This is the example for romance.
# ```{figure} ../../../images/two_scales/p_2sca_Romance.png
# :name: figure-example
# ```
