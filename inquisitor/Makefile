PORTNAME=	inquisitor
DISTVERSION=	28.12a9ec1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT Gathering Tool for Companies and Organizations.
WWW=		https://github.com/penafieljlm/inquisitor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-google-api-client@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-unidecode@${PY_FLAVOR} \
		??/py-unqlite@${PY_FLAVOR} \
		??/py-validate-email@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
