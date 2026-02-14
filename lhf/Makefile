PORTNAME=	lhf
DISTVERSION=	40.51568ee
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular recon tool for pentesting.
WWW=		https://github.com/blindfuzzy/LHF

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/arachni \
		??/dirb \
		??/enum4linux \
		??/hydra \
		??/nikto \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/sqlmap \
		lang/python3 \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
