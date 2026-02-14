PORTNAME=	datasploit
DISTVERSION=	369.28d9caf
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Performs automated OSINT and more.
WWW=		https://github.com/upgoingstar/datasploit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-anyjson@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-billiard@${PY_FLAVOR} \
		??/py-celery@${PY_FLAVOR} \
		??/py-clearbit@${PY_FLAVOR} \
		??/py-configobj@${PY_FLAVOR} \
		??/py-django@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-json2html@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-praw@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-requests-file@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tweepy@${PY_FLAVOR} \
		??/py-wappalyzer@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
