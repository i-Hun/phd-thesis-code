library("feather")
library("lme4")
library("lmerTest")
library("ggplot2")
library("sjPlot")
require(MuMIn)

df <-  read_feather("/Users/hun/Google Drive/HSE/PhD/PhD thesis/data/df_regr.feather")
head(df)
names(df)

df$document.id = as.factor(df$document.id)
df$represent_ethicity_meaning_value = as.factor(df$represent_ethicity_meaning_value)
df$eth_group_to_code = as.factor(df$eth_group_to_code)
df$assessor = as.factor(df$assessor)

model = lmer(opinion_about_ethnonym_recoded_value ~ 
               represent_ethicity_meaning_value +
               (represent_ethicity_meaning_value|eth_group_to_code) +
               (represent_ethicity_meaning_value|assessor) +
               (represent_ethicity_meaning_value|document.id),
             data=df, REML = F)

summary(model)

fixef(model)
ranef(model)

plot(ranef(model)$eth_group_to_code)

sjp.lmer(model, sort = "(Intercept)")

sjp.lmer(model, type = "re.qq")

model2 = lmer(opinion_about_ethnonym_recoded_value ~ 
               represent_ethicity_meaning_value +
               (represent_ethicity_meaning_value|eth_group_to_code) +
               (represent_ethicity_meaning_value|document.id),
              data=df, REML = F)
summary(model2)
anova(model, model2)

# A general and simple method for obtaining R2 from generalized linear mixed-effects models” by Shinichi Nakagawa and Holger Schielzeth
# marginal Rupdate.packages() squared and conditional R squared
# conditional R2 describes the proportion of variance explained by both the fixed and random factors
# marginal R2 and describes the proportion of variance explained by the fixed factor(s) alone

r.squaredGLMM(model)


# ОТНОШЕНИЕ В ЗАВИСИМОСТИ ОТ ЭТНИЧЕСКОЙ ГРУППЫ
model_sent_eth = lmer(opinion_about_ethnonym_recoded_value ~ 
               eth_group_to_code +
               (1|document.id),
             data=df, REML = F)

summary(model_sent_eth)
