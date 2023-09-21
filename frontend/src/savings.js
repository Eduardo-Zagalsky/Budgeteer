const Savings = () => {
    // hardcoded time, balance, apy
    let num = 10000;
    let balance = num.toLocaleString();
    let apy = 4.25;
    let formula = 72 / apy;
    let time = Math.ceil(formula);
    return (
        <div>
            <h1>Savings/Investments</h1>
            <h4>This is a very important tab, because it will teach you how to be financially independent</h4>
            <h3>Savings Accounts</h3>
            <p>The most important thing you need to know about a savings account is <b>THE RULE OF 72</b>, the idea is that if you divide
                72 by the interest rate, or APY, it'll tell you how long it will take for your money to double</p>
            <p><b>Your current balance of ${balance} would take {time} to double at the interest rate of {apy}%</b></p>
            <hr />
            <h3>Investment Accounts</h3>
            <p>Though it is always better to talk to a investment banker about any investment decisions, currently the market is flooded with do it
                yourself apps, so the only big advice here is that, you will want to find stocks that have dividends paid out every certain
                time period and you will want to set them up as a <b>D.R.I.P.=dividend reinvestment plan</b>. Cash dividends earned are reinvested to
                purchase additional shares automatically and commission-free. It allows you to save time and money by reinvesting in your investments.
            </p>
            <hr />
            <h3>IRAs</h3>
            <p>
                There are a few options when it comes to this conversation, 401k vs IRA is a big topic. On the one hand your employer sponsored plan usually
                comes with matching contributions and higher contribution limits, but when you leave you might forget it or they might make it difficult to
                take it with you. An IRA on the other hand has a lower contribution limit but has a lot more flexibility and investment options, as well as
                having the ROTH option.</p>
            <p><b>ROTH IRA:</b> This is an after-tax retirement account, unlike 401k and traditional IRA, this means that you invest into this account
                having already paid the taxes and allowing you to grow your investments <b>tax-free</b>.Let's say you deposit $1,000 now,
                you pay your taxes on that money upfront, and then you invest that money and watch it grow exponentially. When you're over 59 and a half years
                old you'll be able to start withdrawing from that money tax-free. Having paid taxes on the $1,000 dollars you deposited, now you can withdraw
                your $1 million and pay no taxes on any of it.
            </p>
        </div>
    )
}
export default Savings;