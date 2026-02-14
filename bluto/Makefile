PORTNAME=	bluto
DISTVERSION=	142.25cad7a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Recon, Subdomain Bruting, Zone Transfers.
WWW=		https://github.com/darryllane/Bluto

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dnspython2@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-oletools@${PY_FLAVOR} \
		??/py-pdfminer@${PY_FLAVOR} \
		??/py-python2whois@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
