stock_data <- read.csv("stock_data.csv")

# Bar plot of percent change
png("bar_pct_change.png", width = 800, height = 400)
barplot(
  stock_data$PctChange,
  names.arg = stock_data$Day,
  xlab = "Day",
  ylab = "Percent Change",
  main = "Daily Percent Change",
  col  = "steelblue"
)
dev.off()

# Histogram of percent change
png("hist_pct_change.png", width = 800, height = 400)
hist(
  stock_data$PctChange,
  breaks = 15,
  main = "Histogram of Daily Percent Change",
  xlab = "Percent Change",
  col  = "orange",
  border = "white"
)
dev.off()

# Scatter plot of Close with signals
cols <- ifelse(
  stock_data$Signal == "BUY",  "green3",
  ifelse(stock_data$Signal == "SELL", "red3", "gray40")
)

png("scatter_close_signals.png", width = 800, height = 400)
plot(
  stock_data$Day,
  stock_data$Close,
  col = cols,
  pch = 19,
  main = "Close Price by Day with Signals",
  xlab = "Day",
  ylab = "Close Price"
)
legend(
  "topleft",
  legend = c("BUY", "SELL", "HOLD"),
  col    = c("green3", "red3", "gray40"),
  pch    = 19,
  bty    = "n"
)
dev.off()
