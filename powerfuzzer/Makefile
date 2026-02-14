PORTNAME=	powerfuzzer
DISTVERSION=	1.beta
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Powerfuzzer is a highly automated web fuzzer based on many other Open Source fuzzers available (incl. cfuzzer, fuzzled, fuzzer.pl, jbrofuzz, webscarab, wapiti, Socket Fuzzer). It can detect XSS, Injections (SQL, LDAP, commands, code, XPATH) and others.
WWW=		http://www.powerfuzzer.com

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-utidylib@${PY_FLAVOR} \
		??/wxpython \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
