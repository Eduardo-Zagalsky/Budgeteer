const Savings = (props) => {
    return (
        <div>
            <h1>Savings/Investments</h1>
            <p>this is a very important tab because it will teach you the necessary steps to be financially independent</p>
            <h3>Savings Accounts</h3>
            <p>the most important thing you need to know about a savings account is <b>THE RULE OF 72</b>, basically the idea is that if you divide
                72 by the interest rate or APY percentage it'll tell you how long it will take for your money to double</p>
            <p>your current balance of {balance} would take {time} to double at the interest rate of {apy}</p>
            <hr />
            <h3>Investment Accounts</h3>
            <p>Thought it is always better to talk to a investment banker about any investment decisions, currently the market is flooded with do it
                yourself apps, so the only big advice here is that ideally you will want to find stocks that have dividends paid out every certain
                time period and you will want to set them up as a <b>D.R.I.P.=dividend reinvestment plan</b>. cash dividends earned are reinvested to
                purchase additional shares automatically and commission-free. it allows you to save time and money by reinvesting in you investment.
            </p>
            <hr />
            <h3>IRAs</h3>
            <p>
                There are a few options when it comes to this conversation, 401k vs IRA is a big topic, on the one hand your employer sponsored plan usually
                comes with matching contributions and higher contribution limits, but when you leave you might forget it or they might make it difficult to
                take it with you. An IRA on the other hand has a lower contribution limit but has a lot more flexibility and investment options, as well as
                having the ROTH option.
                <b>ROTH IRA:</b> This is an after-tax retirement account, unlike 401k and traditional IRA, this means that you invest into this account
                having already paid the taxes and allowing you to grow your investments <b>tax-free</b> this means, let's say you deposit 1,000 dollars now
                you pay your taxes on that money upfront and then you invest that money and watch it grow exponentially, when you're over 59.5 years old
                you'll be able to start withdrawing from that money tax-free having paid taxes on 1,000 dollars now you can withdraw your 1 million and pay
                no taxes on any of it. something you would need to do on your 401k.
            </p>
        </div>
    )
}