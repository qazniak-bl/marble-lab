library(ggplot2)
library(dplyr)

raw <- read.csv('velocity.csv',header=TRUE)
grouped <- dplyr::group_by(raw,type)

# make plot
fig <- ggplot(raw, aes(t, v_ms, colour=type)) +
    geom_hline(yintercept=0,colour="gray70") +
    geom_point() +
    geom_smooth(method="lm",se=FALSE) +
    theme_bw(base_size=8) + 
    xlab('$t$, \\unit{\\second}')+
    ylab('$v$, \\unit{\\meter\\per\\second}')+
    theme(legend.position="inside",
	legend.position.inside=c(0.95,0.95),
	legend.justification.inside=c("right","top"),
	legend.title=element_blank(),
	legend.key.size=unit(4,"pt"),
	axis.title.y=element_text(margin=margin(t=0,r=5,b=0,l=0,unit="pt")))

# save the figure
ggsave("fig2.svg", plot=fig, width=3.4167, height=2, units="in")

# print stats for linear fits
print(summary(lm(v_ms~t,filter(raw,type=='water'))))
print(summary(lm(v_ms~t,filter(raw,type=='rocks'))))

# use ANOVA to check if differences are significant
model1 <- lm(v_ms~t, data=raw)
model2 <- lm(v_ms~t+type, data=raw)
print(anova(model1,model2))


