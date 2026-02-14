PORTNAME=	belati
DISTVERSION=	72.49577a1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Traditional Swiss Army Knife for OSINT.
WWW=		https://github.com/aancw/Belati

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-api-dnsdumpster@${PY_FLAVOR} \
		??/py-argparse@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cmd2@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-django@${PY_FLAVOR} \
		??/py-dnsknife@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-futures@${PY_FLAVOR} \
		??/py-geoip-geolite2@${PY_FLAVOR} \
		??/py-geoip@${PY_FLAVOR} \
		??/py-pip@${PY_FLAVOR} \
		??/py-pyexifinfo@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-texttable@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-validators@${PY_FLAVOR} \
		??/py-wappalyzer@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
